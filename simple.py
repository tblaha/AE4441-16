"""
Created on Fri Nov 13 11:34:21 2020

@author: tblaha
"""

from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np

import gurobipy as gp
from gurobipy import GRB

#%% import libraries with the class definitions and some config

from Lib import ev_sys
from Lib import grid
from Lib import SimConfig as cfg
from Lib import cars as crs


#%% create new model


# grid config
# create new model ("simple model") sm:
sm = gp.Model("Simple Model")

# set minimization:
sm.ModelSense = 1   # -1 would be maximization


#%% deal with car variables and constraints

# create list of cfg.N identical car object instances
cars = list()
for i in range(0,crs.cars_data['Car Type'].size):
    cars.append(  ev_sys.car(  str(i),  # car name
                               crs.cars_data['Distance Driven'][i],  # km driven per day
                               crs.cars_data['kWh/km'][i], # kWh/km during driving
                               crs.cars_data['Battery size'][i],  # kWh battery size
                               list(crs.cars_t_data['Grid availability'][i*cfg.K:(i+1)*cfg.K]),  # charger type connection to grid per timeslot                
                               )
                )
#%% create grid object
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
SimpleNet = grid.net([200000, 90000, 300000, 40000, 40000, 30000, 20000, 80000],  # kWh sustainable power max supply
                     [1, 1, 1, 1, 1, 1, 1, 1],  # relative cost of sustainable power
                     [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000], # kWh unsustainable power max supply
                     [2, 2, 2, 2, 2, 2, 2, 2],  # relative cost of unsustainable power
                     [0, 0, 0, 0, 0, 20, 0, 0],  # kWh invariant customer demand
                     )

# add power supply variables PS and PU to the model sm
SimpleNet.create_vars_obj(sm)  # also generates objective coefficients
# add the node flow constraint to the model sm
SimpleNet.create_constrs(sm, cars)

#%% solve

sm.optimize()



#%% clean up

# maybe needed, maybe not...
# gp.disposeDefaultEnv()

#%% clean up

# gp.disposeDefaultEnv()