#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:41:26 2020

@author: tblaha
"""

import numpy as np
import pandas as pd
from gurobipy import GRB

# import the global config
from Lib import SimConfig as cfg


#%% Network class definition

class net:
    def __init__(self,
                 grid,       # grid pandas dataframe <-- grid_gen.py
                 grid_links_base,
                 grid_links, # grid connections     <-- grid_gen.py
                 pp_data_base,
                 pp_data,    # powerplant dataframe  <-- pp_gen.py
                 cons_data_base,
                 cons_data,  # Consumer dataframe    <-- cons_gen.py
                 cs,         # cost of sustainable   <-- SimConfig
                 cu,         # cost of unsustainable <-- SimConfig
                 ):
        """ cs, cu  ---> list of length cfg.K (the amount of timeslots)
            """
            
        self.grid = grid
        self.grid_links_base = grid_links_base
        self.grid_links = grid_links
        self.pp_data_base = pp_data_base
        self.pp_data = pp_data
        self.cons_data_base = cons_data_base
        self.cons_data = cons_data
        self.cs = cs
        self.cu = cu
        
        
        
    def create_vars_obj(self, 
                        model,  # the gurobi model to which to add the vars
                        ):
        """ Add the variables for the powerplants supplies to model.
        Also, generate their coefficients in the objective function row.
        
        It's using the "create_vars_obj" method of the powerplant object, 
        defined below
        """
        
        # link variables
        self.links = []
        for index, row in self.grid_links_base.iterrows():
            l_temp = link(row["LinkId"],
                          row["conn1"],
                          row["conn2"],
                          row["Cap"],
                          )
            l_temp.create_vars_obj(model)
            
            self.links.append(l_temp)
            
        
        # list of power plants
        self.PPs = []
        for index, row in self.pp_data_base.iterrows():
            xsecs = self.pp_data.loc[self.pp_data["Name"] == index]
            
            caps = xsecs["Cap"].to_numpy()
            cost = self.cs if row["Sustainability"] == "sustainable" \
                           else self.cu
            
            pp_temp = powerplant(row["Name"],
                                 caps,
                                 cost,
                                 )
            pp_temp.create_vars_obj(model)
            
            self.PPs.append(pp_temp)
            
            
    
    def create_nodal_constrs(self,
                             model,
                             cars,
                             cars_data,
                             ):
        
        grid = self.grid
        grid_links_base = self.grid_links_base
        cons_data = self.cons_data
        pp_data_base = self.pp_data_base
        
        for index, row in self.grid.iterrows():
            # demand
            n_d = cons_data.loc[cons_data["GridConn"] == index,
                                "Load"]
            
            # links
            n_l_idx = grid_links_base.loc[grid_links_base["conn1"] == index,
                                          "LinkId"]
            p_l_idx = grid_links_base.loc[grid_links_base["conn2"] == index,
                                          "LinkId"]
            
            # power plants
            p_p_idx = pp_data_base.loc[pp_data_base["GridConn"] == index, 
                                       "PPId"]
            
            
            for j in range(cfg.K):
                # sum of customer demands at this location
                d_sum = -n_d.iat[j]
                
                # sum of links
                l_sum = ( sum([ self.links[i].L[j] for i in p_l_idx ])
                             - sum([ self.links[i].L[j] for i in n_l_idx ])
                             )
                
                # sum of power plants at this location
                p_sum = sum([ self.PPs[i].P[j] for i in p_p_idx ])
                
                
                # sum of cars --> positive charging is negative for the grid
                #
                # find (time dependent) indices first
                c_idx = cars_data.loc[(cars_data["Time"] == j) 
                                      & (cars_data["GridConn"] == index),
                                      "CarId"
                                      ]
                
                # sum up cars
                # TODO: Implement Power Loss Here!!!
                c_sum = -sum([cars[i].Xi[j] for i in c_idx])
                
                
                # finally: add constraint
                model.addConstr(d_sum + l_sum + p_sum + c_sum == 0,
                                name="C_nodal_" + index + "_" + str(j),
                                )
                


#%% Powerplant class that is mentioned and instantiated above

class powerplant:
    
    def __init__(self, 
                 name,
                 p_s,  # supply capabilities
                 c,    # cost
                 ):
        """ implements the variable/objective/constraint generation for a 
        powerplant with :
            a name
            supply capabilities "p_s"
            supply cost "c"
            """
            
        # save inputs in internal memory
        self.name = name
        self.p_s = p_s
        self.c = c
        
        
    def create_vars_obj(self, model):
        """ Add the supply variables to "model", for each different timeslot
        (ps_j and pu_j) with their bounds and with their contribution to the 
        objective function.
            """
        
        self.P = list()
        for j in range(cfg.K):  # for each time slot j:
                
            # this does the heavy lifting of adding the vars to model
            lb = -self.p_s[j] if self.name == "Cable" else 0.0
            p = model.addVar( 
                    lb = lb,
                    ub = self.p_s[j],  # upper bound: 
                    obj = self.c[j] * cfg.dt[j], # coefficient in objective function
                    vtype=GRB.CONTINUOUS,
                    name="P_" + self.name + "_" + str(j)
                    )
                
            # this only saves the gurobi variable objects to a list for future 
            # reference in the node constraints
            self.P.append(p)
            
        return self.P
            

#%% links

class link():
    def __init__(self,
                 name, 
                 conn1,
                 conn2,
                 cap,
                 ):
        
        self.name = name
        self.conn1 = conn1
        self.conn2 = conn2
        self.cap = cap
        
    def create_vars_obj(self, model):
        self.L = list()
        for j in range(cfg.K):
            
            # this does the heavy lifting of adding the vars to model
            l = model.addVar(
                    lb = -self.cap,
                    ub = +self.cap,
                    obj = 0,   # TODO: fix this with some sort of 
                               # regularization so we don't get speedy 
                               # currents running round in circles...
                    vtype = GRB.CONTINUOUS,
                    name = "L_" + str(self.name) + "-" + self.conn1 + "-" + self.conn2 + "_" + str(j),
                    )
                
            # this only saves the gurobi variable objects to a list for future 
            # reference in the node constraints
            self.L.append(l)
        
        return self.L
    





