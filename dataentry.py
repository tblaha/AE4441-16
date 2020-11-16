#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:34:21 2020

@author: tblaha
"""

# from IPython import get_ipython
# get_ipython().magic('reset -sf')

import numpy as np

import gurobipy as gp
from gurobipy import GRB

from DataEntryLib import ev_sys
from DataEntryLib import grid
from DataEntryLib import config as cfg
from DataEntryLib import cars as crs


# grid config
ps_s = [2000, 4000, 4000, 2000]  # kWh sustainable power
pu_s = [10000, 10000, 10000, 10000]  # kWh unsustainable power
pd = [0, 0, 0, 0]  # kWh custumer demand

cs = [1, 1, 1, 1]  # relative cost of sustainable power
cu = [2, 2, 2, 2]  # relative cost of unsustainable power


#%% create car objects

# create list of (identical) car objects
cars = list()
for i in range(sum(crs.car_stat['Amount owned'])):
    cars.append(  ev_sys.car(  str(i),  # car name
                               crs.cars_data['Distance Driven'][i],  # km driven per day
                               crs.cars_data['kWh/km'][i]/10, # kWh/km during driving
                               crs.cars_data['Battery size'][i],  # kWh battery size
                               [crs.cars_data['Grid connection 1'][i],crs.cars_data['Grid connection 2'][i],crs.cars_data['Grid connection 3'][i], crs.cars_data['Grid connection 4'][i]],  # connection to grid per timeslot
                               crs.cars_data['Charger type'][i],   # charger type
                               )
                )

#%% create grid object
AdvancedNet = grid.net(ps_s, cs, pu_s, cu, pd)


#%% setup model

# create new model ("advanced model") sm:
am = gp.Model("Advanced Model")

# deal with car variables and constraints
X = list()
Y = list()
C_cars = list()
for car in cars:
    X_i, Y_i = car.create_vars(am)
    X.append(X_i)
    Y.append(Y_i)
    
    C_cars.append(car.create_constrs(am))
    
# deal with net variables and bounds and objective coefficients
PS, PU = AdvancedNet.create_vars_obj(am)  # also generates objective coefficients

# deal with net constraint
C_node = AdvancedNet.create_constrs(am, X)

# objective function is already generated in the net variable creation
# so, only set sense:
am.ModelSense = 1   # -1 would be maximization


#%% solve

am.optimize()


#%% clean up

# gp.disposeDefaultEnv()
