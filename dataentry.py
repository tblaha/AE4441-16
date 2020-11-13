#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:34:21 2020

@author: tblaha
"""

from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np

import gurobipy as gp
from gurobipy import GRB

from SimpleLib import ev_sys
from SimpleLib import grid
from SimpleLib import config as cfg


# grid config
ps_s = [2, 4, 4, 2]  # kWh sustainable power
pu_s = [10, 10, 10, 10]  # kWh unsustainable power
pd = [0, 0, 0, 0]  # kWh custumer demand

cs = [1, 1, 1, 1]  # relative cost of sustainable power
cu = [2, 2, 2, 2]  # relative cost of unsustainable power


#%% create car objects

# create list of (identical) car objects
cars = list()
for i in range(cfg.N):
    cars.append(ev_sys.car(str(i),  # car name
                           20,  # km driven per day
                           0.2, # kWh/km during driving
                           40,  # kWh battery size
                           [1, 1, 0, 1],  # connection to grid per timeslot
                           1,   # charger type
                           )
                )

#%% create grid object
SimpleNet = grid.net(ps_s, cs, pu_s, cu, pd)


#%% setup model

# create new model ("simple model") sm:
sm = gp.Model("Simple Model")

# deal with car variables and constraints
X = list()
Y = list()
C_cars = list()
for car in cars:
    X_i, Y_i = car.create_vars(sm)
    X.append(X_i)
    Y.append(Y_i)
    
    C_cars.append(car.create_constrs(sm))
    
# deal with net variables and bounds and objective coefficients
PS, PU = SimpleNet.create_vars_obj(sm)  # also generates objective coefficients

# deal with net constraint
C_node = SimpleNet.create_constrs(sm, X)

# objective function is already generated in the net variable creation
# so, only set sense:
sm.ModelSense = 1   # -1 would be maximization


#%% solve

sm.optimize()


#%% clean up

# gp.disposeDefaultEnv()
