#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:33:12 2020

@author: tblaha
"""

import numpy as np
from gurobipy import GRB

from Lib import SimConfig as cfg


#%% Car class
class car:
    """ Electriv vehicle class characterizing owner and charger
    """
    def __init__(self, 
                 name,      # string for identifying the car
                 s_day,     # km driven during the day
                 E_eff,     # kWh electrical energy used per km
                 E_bat,     # battery size in kWh
                 P_max,     # charger max power in both directions
                 t_conn,    # list of timeslots connected to grid
                 ):
        """
        name should be a string
        s_day, E_eff, E_bat, P_max should be scalars
        t_conn should be a list of 0s and 1s indicated when the EV is connected
            """
        
        # saving input in internal memory 
        self.name  = name
        self.s_day = s_day  # km/day
        self.E_eff = E_eff  # kWh/km
        
        # set energy limits to within 10% - 90% of nominal battery capacity
        self.E_max = 0.9*E_bat  # kWh
        self.E_min = 0.1*E_bat  # kWh
        
        # Battery charge at beginning of the day
        self.E_state = 0.5*(self.E_max + self.E_min)
        
        # max charger power 
        self.P_max = P_max
        
        # convert t_conn list to a proper boolean array
        self.t_conn = np.array(t_conn).astype(bool)  # bool
        
        
#%% Variables and Bounds
    def create_vars(self, 
                    model,  # the gurobi model to which to add the vars to
                    ):
        """ Add the variables for the EVs to model (ie the charger powers for 
        each time slot j)
            """
        
        self.Xi = list()
        for j in range(cfg.K):  # for each time slot j:
            
            # CONTINUOUS charging power variable
            # this does the heavy lifting of adding to model
            x = model.addVar(
                lb = -self.P_max,
                ub = +self.P_max,
                obj = 0.0, # not in obj directly (see create_constrs of grid.py)
                vtype=GRB.CONTINUOUS,
                name="X_" + self.name + "_" + str(j)
                )
            
            # this is only for later use of the vars in the constraints
            self.Xi.append(x)
            
        return self.Xi
    
    
#%% Constraints
    def create_constrs(self, 
                       model,  # the gurobi model to which to add the constrs
                       ):
        
        # changing power can only be non-zero if the EV is actually connected
        for j in range(cfg.K):  # for each time slot j
            # if NOT connected --> X_ij * 1 == 0
            # if connected     --> X_ij * 0 == 0; hope for the best
            model.addConstr(
                self.Xi[j] * (~self.t_conn[j]) == 0,
                name="C_" + self.name + "_" + str(j) + "_conn"
                )
        
        # for each car, the net energy supplied to the battery over the day
        # must be positive; so that we cannot end up with a car that is 
        # drained more than at the start of the day
        model.addConstr(
            sum( # sum of list-comprehension of all time slots j
                self.Xi[j] * cfg.dt[j] # Bat energy changed in timeslot j
                for j in range(cfg.K)
                )
               >= self.E_eff * self.s_day,
           name="C_" + self.name + "_E_net"
           )
        
        for j in range(cfg.K - 1):  # for each time slot j
            # after each time step j, car battery may not go below E_min
            model.addConstr( 
                self.E_state  # initial battery energy
                + sum( # sum of list-comprehension of all time slots UP UNTIL j
                    self.Xi[jj] * cfg.dt[jj] # Bat energy changed in timeslot jj
                    for jj in range(j + 1)
                    )
                >= self.E_min,
                name="C_" + self.name + "_" + str(j) + "_E_lb"
                )
            
            # after each time step j, car battery may not go above E_max
            model.addConstr(  
                self.E_state  # initial battery energy
                + sum( # sum of list-comprehension of all time slots UP UNTIL j
                    self.Xi[jj] * cfg.dt[jj] # Bat energy changed in timeslot jj
                    for jj in range(j + 1)
                    )
                <= self.E_max,
                name="C_" + self.name + "_" + str(j) + "_E_ub"
                )
