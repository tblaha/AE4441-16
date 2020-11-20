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
import pandas as pd
import matplotlib.pyplot as plt

import gurobipy as gp
from gurobipy import GRB


#%% import libraries with the class definitions and some config

from Lib.cars import car_stat, cars_data, grid
from Lib import ev_sys
from Lib import grid as gd
from Lib import SimConfig as cfg
from Lib import plotting as pt


#%% empty gurobi model

# create new model ("advanced model") am:
am = gp.Model("Advanced Model")

# objective function is already generated in the net variable creation
# so, only set sense:
am.ModelSense = 1   # -1 would be maximization



#%% deal with car variables and constraints

# create list of car objects
cars = list()
for i in range(sum(car_stat['Amount owned'])):
    # figure out which lines in the cars_data frame belong to car i
    car_bool = cars_data["CarId"] == i
    
    cars.append(ev_sys.car(
        str(i),  # car name
        cars_data.loc[car_bool, 'Distance Driven'].iat[0],  # km driven per day
        cars_data.loc[car_bool, 'kWh/km'].iat[0], # kWh/km during driving
        cars_data.loc[car_bool, 'Battery size'].iat[0],  # kWh battery size
        #cars_data.loc[car_bool, 'GridNode'],  # connection to grid per timeslot
        cars_data.loc[car_bool, 'Charger type'].to_numpy(),   # charger type
        ))

# deal with car variables and constraints
X = list()
Y = list()
C_cars = list()
for car in cars:
    X_i, Y_i = car.create_vars(am)
    X.append(X_i)
    Y.append(Y_i)
    
    C_cars.append(car.create_constrs(am))



#%% grid config
ps_s = 100*np.ones(cfg.K)  # kWh sustainable power
pu_s = 500*np.ones(cfg.K)  # kWh unsustainable power
p_d = 0*np.ones(cfg.K)  # kWh custumer demand

cs = 1*np.ones(cfg.K)  # relative cost of sustainable power
cu = 2*np.ones(cfg.K)  # relative cost of unsustainable power

# create grid object
AdvancedNet = gd.net(ps_s, cs, pu_s, cu, p_d)

# deal with net variables and bounds and objective coefficients
AdvancedNet.create_vars_obj(am)  # also generates objective coefficients

# deal with net constraint
C_node = AdvancedNet.create_constrs(am, cars)



#%% solve

am.optimize()

# print()
# for Xi in X:
#     for Xij in Xi:
#         print(Xij)



#######################################
#%% Post Proc Results
#######################################

#%% dummy data: grid connection

grid_conn = pd.DataFrame(columns=["conn1",
                                  "conn2", 
                                  "Cap",
                                  "time",
                                  "Load"]
                         )
grid_conn = grid_conn.astype({"conn1": str, 
                              "conn2": str, 
                              "Cap": float, 
                              "time": int, 
                              "Load": float,
                              })

# grid_conn.loc[1] = ["Ronne", "Nexo", 100, 0, 70]
# grid_conn.loc[2] = ["Ronne", "Tejn", 100, 0, 110]
# grid_conn.loc[3] = ["Nexo", "Tejn", 100, 0, -70]
# grid_conn.loc[4] = ["Ronne", "Nexo", 100, 1, 0]
# grid_conn.loc[5] = ["Ronne", "Tejn", 100, 1, 50]
# grid_conn.loc[6] = ["Nexo", "Tejn", 100, 1, -35]
# grid_conn.loc[7] = ["Ronne", "Nexo", 100, 2, 105]
# grid_conn.loc[8] = ["Ronne", "Tejn", 100, 2, 97]
# grid_conn.loc[9] = ["Nexo", "Tejn", 100, 2, 98]



#%% post process solution


# temporary data for testing visualization
for i, car in enumerate(cars):
    # figure out which lines in the cars_data frame belong to car i
    car_bool = cars_data["CarId"] == i
    
    # add the charging load
    cars_data.loc[car_bool, "Load"] = np.array([Xtemp.X for Xtemp in car.Xi])
    cars_data.loc[car_bool, "Cap"]  = 11



#%% plotting

outpath = "./plots/"
fnamebase = "test"

map_extent = [14.65, 15.2, 54.97, 55.31]; zoomlevel = 10; # all of Bornholm
# map_extent = [14.66, 14.76, 55.07, 55.125]; zoomlevel = 13; # Ronne

c = pt.netgif(map_extent, zoomlevel)  # Ronne
c.plot_series(grid, grid_conn, cars_data, gd.pp_data, gd.cons_data, outpath, fnamebase)

plt.close("all")



#%% clean up

# maybe needed, maybe not...
# gp.disposeDefaultEnv()















