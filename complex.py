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

from Lib.cars_gen import car_stat, cars_data_base, cars_data
from Lib.grid_gen import grid, grid_links_base, grid_links
from Lib.pp_gen   import pp_data_base, pp_data
from Lib.cons_gen import cons_data_base, cons_data

from Lib import cars as cs
from Lib import grid as gd
from Lib import SimConfig as cfg

try:
    import cartopy
    cartopy_exists = True
    from Lib import plotting as pt
except ImportError:
    cartopy_exists = False




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
    
    cars.append(cs.car(
        str(i),  # car name
        cars_data.loc[car_bool, 'Distance Driven'].iat[0],  # km driven per day
        cars_data.loc[car_bool, 'kWh/km'].iat[0], # kWh/km during driving
        cars_data.loc[car_bool, 'Battery size'].iat[0],  # kWh battery size
        #cars_data.loc[car_bool, 'GridNode'],  # connection to grid per timeslot
        cars_data.loc[car_bool, 'Charger type'].to_numpy(),   # charger type
        ))

# deal with car variables and constraints
for car in cars:
    car.create_vars(am)
    car.create_constrs(am)



#%% grid config
# ps_s = 100*np.ones(cfg.K)  # kWh sustainable power
# pu_s = 500*np.ones(cfg.K)  # kWh unsustainable power
# p_d = 0*np.ones(cfg.K)  # kWh custumer demand

cs = 1*np.ones(cfg.K)  # relative cost of sustainable power
cu = 2*np.ones(cfg.K)  # relative cost of unsustainable power

# create grid object
AdvancedNet = gd.net(grid,
                     grid_links_base,
                     grid_links,
                     pp_data_base,
                     pp_data,
                     cons_data_base,
                     cons_data,
                     cs,
                     cu,
                     )



#%%
# deal with net variables and bounds and objective coefficients
AdvancedNet.create_vars_obj(am)  # also generates objective coefficients

# deal with net constraint
AdvancedNet.create_nodal_constrs(am, cars, cars_data)



#%% solve

am.optimize()


#######################################
#%% Post Proc Results
#######################################


#%% post process solution


# temporary data for testing visualization
for i, car in enumerate(cars):
    # figure out which lines in the cars_data frame belong to car i
    car_bool = cars_data["CarId"] == i
    
    # add the charging load
    cars_data.loc[car_bool, "Load"] = np.array([Xtemp.X for Xtemp in car.Xi])
    cars_data.loc[car_bool, "Cap"]  = 11

for i, pp in enumerate(AdvancedNet.PPs):
    pp_bool = pp_data["PPId"] == i
    
    pp_data.loc[pp_bool, "Load"] = np.array([Xtemp.X for Xtemp in pp.P])

for i, l in enumerate(AdvancedNet.links):
    l_bool = grid_links["LinkId"] == i
    
    grid_links.loc[l_bool, "Load"] = np.array([Xtemp.X for Xtemp in l.L])


#%% plotting

if cartopy_exists:
    outpath = "./plots/"
    fnamebase = "test"
    
    map_extent = [14.65, 15.2, 54.97, 55.31]; zoomlevel = 10; # all of Bornholm
    # map_extent = [14.66, 14.76, 55.07, 55.135]; zoomlevel = 13; # Ronne
    
    netplot = pt.netgif(map_extent, zoomlevel)  # Ronne
    netplot.plot_series(grid, grid_links, cars_data, pp_data, cons_data, outpath, fnamebase)
    
    plt.close("all")



#%% clean up

# maybe needed, maybe not...
# gp.disposeDefaultEnv()
dellist = ["car", "fnamebase", "i", "l", "l_bool", "map_extent", 
           "outpath", "pp_bool", "zoomlevel"]

for delitem in dellist:
    try:
        del globals()[delitem]
    except:
        pass

del dellist
del delitem












