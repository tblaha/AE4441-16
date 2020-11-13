#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:41:26 2020

@author: tblaha
"""

import numpy as np
from gurobipy import GRB

# import the global config
from Lib import SimConfig as cfg


#%% Network class definition

class net:
    def __init__(self,
                 ps_s,  # available sustainable power supply for each time j
                 cs,    # cost of sustainable power for each time j
                 pu_s,  # available UNsustainable power supply for each time j
                 cu,    # cost of UNsustainable power for each time j
                 pd,    # invariant consumer demand for each time j
                 ):
        """ ps_s, cs, pu_s, cu, pd  ---> list of length cfg.K (the amount of 
                                                               timeslots)
        """
        
        # save customer demand in internal memory
        self.pd = pd
        
        # instantiate power-plant objects (defined below) for the supplies
        self.sus_power = powerplant("sus", ps_s, cs)
        self.unsus_power = powerplant("unsus", pu_s, cu)
        
    
    def create_vars_obj(self, 
                        model,  # the gurobi model to which to add the vars
                        ):
        """ Add the variables for the powerplants supplies to model.
        Also, generate their coefficients in the objective function row.
        
        It's using the "create_vars_obj" method of the powerplant object, 
        defined below
        """
        
        # list of Sustainable power variables for each j
        self.PS = self.sus_power.create_vars_obj(model)
        
        # list of Unsustainable power variables for each j
        self.PU = self.unsus_power.create_vars_obj(model)
    
    
    def create_constrs(self, 
                       model,  # the gurobi model to which to add the constrs
                       cars,   # list of car objects
                       ):
        """ Add flow constraint to "model", for each different timeslot, based 
        on a single-node model of the grid (direct connection from/to all 
                                            supplies/demands)
            """
        for j in range(cfg.K):  # for each time slot j:
            model.addConstr(self.PS[j] + self.PU[j]   # supply energy
                == self.pd[j]  # customer demand
                + sum( # sum over all cars
                      cars[i].Xi[j] # battery charging power 
                                    # + dot product of mode binaries and loss 
                                    # list for the different modes
                      + np.array(cars[i].Yi[j]) @ cars[i].ch[j].P_loss 
                      for i in range(cfg.N)
                      ),
                name="C_node_" + str(j),
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
        
        P = list()
        for j in range(cfg.K):  # for each time slot j:
                
            # this does the heavy lifting of adding the vars to model
            p = model.addVar( 
                    lb = 0.0,
                    ub = self.p_s[j],  # upper bound: 
                    obj = self.c[j] * cfg.dt[j], # coefficient in objective function
                    vtype=GRB.CONTINUOUS,
                    name="P_" + self.name + "_" + str(j)
                    )
                
            # this only saves the gurobi variable objects to a list for future 
            # reference in the node constraints
            P.append(p) 
            
        return P
            
            