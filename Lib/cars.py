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
        
        # Battery charge at beginning of the day
        self.E_state = 0.5*(self.E_max + self.E_min)
        
        # instantiate chargers 
        self.Ch_constr = cars_data["Charger type"].to_numpy()
        self.P_chargers\
            = charger_stat[cars_data["Car Type"].iat[0]]\
                .to_numpy().astype(float)
                                
        
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
        for j in range(cfg.K):  # for each time slot j:
            
            # CONTINUOUS charging power variable
            # this does the heavy lifting of adding to model
            x = model.addVar(
                lb = -1e100,
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
                    name="Y_" + self.name + "_" + str(j) + "_" + str(k)
                    )
                Yij.append(y)
            
            self.Yi.append(Yij)
            
        return self.Xi, self.Yi
    
    
    
#%% Constraints
    def create_constrs(self, 
                       model,  # the gurobi model to which to add the constrs
                       ):
        
        # Pmax = 
        
        ## Charging power maximum selection
        ###############################################
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
                # we can freely select one charger that the car will use that
                # day for all time slots with "-1" as charger type
                model.addConstr(
                    sum(self.Yi[j]) <= 1,
                    name="C_OOOM_" + self.name + "_" + str(j),
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
               >= self.E_eff * self.s_day,
           name="C_Enet_" + self.name
           )
        
        for j in range(cfg.K - 1):  # for each time slot j
            # after each time step j, car battery may not go below E_min
            model.addConstr( 
                self.E_state  # initial battery energy
                + sum( # sum of list-comprehension; all time slots UP UNTIL j
                    self.Xi[jj] * cfg.dt[jj] # Energy changed in timeslot jj
                    for jj in range(j+1)
                    )
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
                <= self.E_max,
                name="C_Eub_" + self.name + "_" + str(j)
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