#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:34:21 2020

@author: tblaha
"""

#%% reset python workspace
from IPython import get_ipython
get_ipython().magic('reset -sf')


#%% import modules
import numpy as np

import gurobipy as gp
from gurobipy import GRB


#%% import libraries with the class definitions and some config

from Lib.cars import car_stat, cars_data, grid
from Lib import ev_sys
from Lib import grid
from Lib import SimConfig as cfg


#%% create new model

# create new model ("simple model") sm:
sm = gp.Model("Simple Model")

# set minimization:
sm.ModelSense = 1   # -1 would be maximization


#%% deal with car variables and constraints

# create list of cfg.N identical car object instances
cars = list()
for i in range(cfg.N):
    cars.append(ev_sys.car(str(i),  # car name
                           20,   # km driven per day
                           0.2,  # kWh/km during driving
                           40,   # kWh battery size
                           [1, 1, 0, 2, 2, 2, 0, 1],  # charger type connection to grid per timeslot
                           )
                )

X = list()  # will hold the solutions later
Y = list()  # will hold the solutions later
for car in cars:  # for each car

    # add changing power variable for each timeslot to the model sm
    Xi, Yi = car.create_vars(sm)
    X.append(Xi)
    Y.append(Yi)
    
    # add constraints to the model sm
    car.create_constrs(sm)


#%% deal with power supply and grid

# create grid object
SimpleNet = grid.net([2, 2, 3, 4, 4, 3, 2, 2],  # kWh sustainable power max supply
                     [1, 1, 1, 1, 1, 1, 1, 1],  # relative cost of sustainable power
                     [10, 10, 10, 10, 10, 10, 10, 10], # kWh unsustainable power max supply
                     [2, 2, 2, 2, 2, 2, 2, 2],  # relative cost of unsustainable power
                     [0, 0, 0, 0, 0, 20, 0, 0],  # kWh invariant customer demand
                     )

# add power supply variables PS and PU to the model sm
SimpleNet.create_vars_obj(sm)  # also generates objective coefficients

# add the node flow constraint to the model sm
SimpleNet.create_constrs(sm, cars)


#%% solve

sm.optimize()

print()
for Xi in X:
    for Xij in Xi:
        print(Xij)


#%% clean up

# maybe needed, maybe not...
# gp.disposeDefaultEnv()

