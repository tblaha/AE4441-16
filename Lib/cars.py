#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:33:12 2020

@author: tblaha
"""

import numpy as np
from gurobipy import GRB
#from cars_gen import cars_data, charger_stat

from Lib import SimConfig as cfg


#%% Car class
class car:
    """ Electriv vehicle class characterizing owner and charger
    """
    def __init__(self, 
                 cars_data,
                 charger_stat,
                 ):
        """
        name should be a string
        s_day, E_eff, E_bat, P_max should be scalars
        c_conn should be a list: 0 if no charger, 1-C when the connected
            """
        
        # saving input in internal memory 
        self.name  = str(cars_data["CarId"].iat[0])
        self.s_day = cars_data["Distance Driven"].iat[0]  # km/day
        self.E_eff = cars_data["kWh/km"].iat[0]  # kWh/km
        self.E_bat = cars_data["Battery size"].iat[0]
        
        # set energy limits to within 10% - 90% of nominal battery capacity
        self.E_max = 0.9*self.E_bat  # kWh
        self.E_min = 0.1*self.E_bat  # kWh
        
        # instantiate chargers 
        self.Ch_constr = cars_data["Charger type"].to_numpy()
        self.P_chargers\
            = charger_stat[cars_data["Car Type"].iat[0]]\
                .to_numpy().astype(float)
                
        # Battery charge at beginning of the day
        self.Num_slots_driving_total = sum(self.Ch_constr == 0)
        
        if self.Num_slots_driving_total:
            Slots_driving_evening \
                = sum(self.Ch_constr[np.floor(cfg.K*(2/3)).astype(int):] == 0)
            E_driven_evening\
                = self.s_day * self.E_eff\
                   * Slots_driving_evening / self.Num_slots_driving_total
            self.E_state = np.minimum(self.E_max - E_driven_evening, 
                                      0.5*(self.E_max + self.E_min)
                                      )
        else:
            self.E_state = 0.5*(self.E_max + self.E_min)
                
        
        self.Del = np.array([-1, 1])
        
#%% Variables and Bounds
    def create_vars(self, 
                    model,  # the gurobi model to which to add the vars to
                    ):
        """ Add the variables for the EVs to model:
        Xij: the charger powers for each time slot j
        Yijk: the binarys describing the charging setting to use at instant j
            """
        
        
        self.Xi = list()
        self.Yi = list()
        self.Dxpi = list()
        self.Dxni = list()
        for j in range(cfg.K):  # for each time slot j:
            
            # CONTINUOUS charging power variable
            # this does the heavy lifting of adding to model
            x = model.addVar(
                lb = -1e100, # gurobi manual says do this...
                ub = +1e100,
                obj = 0.0, # not in obj directly (see create_constrs 
                                                # of grid.py)
                vtype=GRB.CONTINUOUS,
                name="X_" + self.name + "_" + str(j),
                )
            
            
            # this is only for later use of the vars in the constraints
            self.Xi.append(x)
            
            # binary charging setting mode variables
            Yij = list()
            for k, __ in enumerate(self.P_chargers):
                y = model.addVar(
                    vtype=GRB.BINARY,
                    obj = 1e-6,
                    name="Y_" + self.name + "_" + str(j) + "_" + str(k)
                    )
                Yij.append(y)
            
            self.Yi.append(Yij)
            
            
            # Derivative variables
            if (j < cfg.K + 1 - len(self.Del)):
                # positive derivatives
                Dxp = model.addVar(
                        lb = 0,
                        ub = +1e100,
                        obj = 1e-6,
                        vtype=GRB.CONTINUOUS,
                        name="Dxp_" + self.name + "_" + str(j),
                        )
                # negative derivatives
                Dxn = model.addVar(
                        lb = 0,
                        ub = +1e100,
                        obj = 1e-6,
                        vtype=GRB.CONTINUOUS,
                        name="Dxn_" + self.name + "_" + str(j),
                        )
                
                self.Dxpi.append(Dxp)
                self.Dxni.append(Dxn)
        
        
        # assign one additional variable to the cars the describe the one 
        # single choice of a charger access at work
        self.Yiwork = []
        for k, __ in enumerate(self.P_chargers):
            y = model.addVar(
                vtype=GRB.BINARY,
                obj=1e-6,
                name="Y_work_" + self.name + "_" + str(k)
                )
            self.Yiwork.append(y)
        
        
        # soft constraint switch for battery limit constraints
        self.SoftCon_E = model.addVar(
                vtype=GRB.BINARY,
                obj=1e9,
                name="S_" + self.name + "_Emin",
                )
        
            
        return self.Xi, self.Yi, self.Yiwork
    
    
    
#%% Constraints
    def create_constrs(self, 
                       model,  # the gurobi model to which to add the constrs
                       ):
        
        
        
        ## Charging power maximum selection
        ###############################################
        # make the algorithm able to assign max _one_ work charger to a car. 
        # This doesn't mean that the car _has_ to have on at work or use it 
        # all the time; it merely means that it may get access to at most one.
        #for k, __ in enumerate(self.P_chargers):
        model.addConstr(
            sum(self.Yiwork) <= 1,
            name="C_OOOMWork_" + self.name,# + "_" + str(k),
            )
        
        
        for j in range(cfg.K):  # for each time slot j
            
            # charger power lower and upper bounds
            model.addConstr(
                self.Xi[j] <= self.P_chargers @ self.Yi[j],
                name="C_Pub_" + self.name + "_" + str(j),
                )
            
            model.addConstr(
                self.Xi[j] >= -self.P_chargers @ self.Yi[j],
                name="C_Plb_" + self.name + "_" + str(j),
                )
            
            # charger selection for each car
            ch = self.Ch_constr[j]
            if ch == -1:
                # that charger that will be used at work is chosed in the 
                # Yiwork binary, so here we need to make sure that that choice
                # is the only possible choice for the relevant hourly binaries
                # Yi[j]
                for k, __ in enumerate(self.P_chargers):
                    model.addConstr(
                        self.Yi[j][k] <= self.Yiwork[k],
                        name="C_WorkAssign_" + self.name + "_" + str(j) + "_" + str(k),
                        )
            elif ch == 0:
                # Car is on the road; no charger, sadface
                model.addConstr(
                    sum(self.Yi[j]) == 0,
                    name="C_OOOM_" + self.name + "_" + str(j),
                    )
            elif ch > 0:
                # Car has a defined charger: 
                # set the chosen one to 1
                model.addConstr(
                    self.Yi[j][ch-1] == 1,
                    name="C_OOOMa_" + self.name + "_" + str(j),
                    )
                
                # set the sum of all other to 0
                model.addConstr(
                    sum([x for i, x in enumerate(self.Yi[j]) if i != (ch-1)])
                        == 0,
                    name="C_OOOMb_" + self.name + "_" + str(j),
                    )
        
        ## Resulting battery energy constraints 
        ################################################
        
        # for each car, the net energy supplied to the battery over the day
        # must be positive; so that we cannot end up with a car that is 
        # drained more than at the start of the day
        model.addConstr(
            sum( # sum of list-comprehension of all time slots j
                self.Xi[j] * cfg.dt[j] # Bat energy changed in timeslot j
                for j in range(cfg.K)
                )
                # + self.SoftCon_E * 1e9
               >= self.E_eff * self.s_day,
               name="C_Enet_" + self.name,
           )
        
        for j in range(cfg.K - 1):  # for each time slot j
            # Energy "lost" by driving at this point in time
            if (self.Ch_constr == 0).any():
                E_lost = sum(self.Ch_constr[0:(j+1)] == 0) \
                            / sum(self.Ch_constr == 0) \
                            * self.E_eff * self.s_day
            else:
                E_lost = 0
            
            # after each time step j, car battery may not go below E_min
            model.addConstr( 
                self.E_state  # initial battery energy
                + sum( # sum of list-comprehension; all time slots UP UNTIL j
                    self.Xi[jj] * cfg.dt[jj] # Energy changed in timeslot jj
                    for jj in range(j+1)
                    )
                - E_lost
                #+ self.SoftCon_E * 1e9
                >= self.E_min,
                name="C_Elb_" + self.name + "_" + str(j)
                )
            
            # after each time step j, car battery may not go above E_max
            model.addConstr(
                self.E_state  # initial battery energy
                + sum( # sum of list-comprehension; all time slots UP UNTIL j
                    self.Xi[jj] * cfg.dt[jj] # Energy change in timeslot jj
                    for jj in range(j+1)
                    )
                - E_lost
                #+ self.SoftCon_E * 1e9
                <= self.E_max,
                name="C_Eub_" + self.name + "_" + str(j)
                )
            
        
        ## Calculate time derivative of charging rate
        ###################################################
        
        # method: use central finite difference stensil Del = [-1 0 1]
        #         then convolve (endpoint exclusive!) the stensil with the 
        #         vector Xi to get (cfg.K - 2) derivatives!
        #         
        for j in range(cfg.K + 1 - len(self.Del)):
            # positive 
            model.addConstr(
                # against all odds this doesn't give errors, because numpy 
                # ignores index bounds for multiselection which is beyond 
                # shitty in terms of robustness and error-on-unexpected 
                # philosophy, but necessary since otherwise there would be
                # no programatic way to select the last N elements of a 
                # vector because [2:] cannot be programmed. This again 
                # shows that inclusive indexing is superior.
                +self.Del @ self.Xi[j:j+len(self.Del)]
                <= self.Dxpi[j],
                name="C_Dxp_" + self.name + "_" + str(j)
                )
            
            # negative
            model.addConstr(
                -self.Del @ self.Xi[j:j+len(self.Del)]
                <= self.Dxni[j],
                name="C_Dxn_" + self.name + "_" + str(j)
                )
        

#%% Charger types
# class charger:
#     def __init__(self, ch_type):
#         if ch_type == 0:
#             # no charger
#             self.M = 1
#             self.P = np.array([0])
#             self.P_loss = self.P
            
#         elif ch_type == 1:
#             # home charger?
#             self.M = 7  # charging modes
#             self.P = np.array([-11, -5, -2, 0, 2, 5, 11])  # kW power
#             self.P_loss = (
#                 self.P # power lost ontop of self.P
#                 * np.array([-0.1, -0.12, -0.15, 0, 0.1, 0.07, 0.06])
#                 )
            
#         elif ch_type == 2:
#             # fast charger?
#             self.M = 5  # charging modes
#             self.P = np.array([-20, -5, 0, 5, 20])  # kW power
#             self.P_loss = (self.P # power lost ontop of self.P
#                            * np.array([-0.05, -0.08, 0, 0.08, 0.03])
#                            )
            
#         else:
#             raise NotImplementedError("Only Charger Types \
#                                        0, 1 and 2 implemented.")
                                       
                                       
                                       
                                       
                                       

# car(cars_data.iloc[0:3], charger_stat)