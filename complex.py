#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:34:21 2020

@author: tblaha
"""

#%% reset python workspace

print("complex.py: Clearing workspace", end='... ')

from IPython import get_ipython
get_ipython().magic('reset -sf')

print("OK!")



#%% import modules

print("complex.py: Importing Modules", end='... ')

#general modules
import numpy as np
import matplotlib.pyplot as plt
import gurobipy as gp

# try importing cartopy for creating of beatuiful and awesome maps
try:
    import cartopy
    cartopy_exists = True
    from Lib import plotting as pt
except ImportError:
    cartopy_exists = False
    
    

# generate and organize the problem data --> actual magic is hidden here
from Lib.cars_gen import car_stat, cars_data_base, cars_data, charger_stat
from Lib.grid_gen import grid, grid_links_base, grid_links
from Lib.pp_gen   import pp_data_base, pp_data
from Lib.cons_gen import cons_data_base, cons_data

# import classes to be used to generate the Gurobi variables/constraints
from Lib import cars as cs
from Lib import grid as gd
from Lib import SimConfig as cfg

print("OK!")



#%% empty gurobi model

print("complex.py: Initialize Gurobi Model", end='... ')


# create new model ("advanced model") am:
am = gp.Model("Advanced Model")

# objective function is already generated in the net variable creation
# so, only set sense:
am.ModelSense = 1   # -1 would be maximization

print("OK!")



#%% deal with car variables and constraints

print("complex.py: Create cars/charger objects, variables and constraints",
      end='... ')


# create list of car objects
cars = list()
for i in range(sum(car_stat['Amount owned'])):
    # figure out which lines in the cars_data frame belong to car i
    car_bool = cars_data["CarId"] == i
    
    cars.append(cs.car(cars_data.loc[car_bool], charger_stat))

# deal with car variables and constraints
for car in cars:
    car.create_vars(am)
    car.create_constrs(am)
    

# a little bit beun to put it here, but oh well... 
# --> amount of away-from-home charger constraints
for j in range(cfg.K):
    # if no cars have work chargers at this time --> no constraint
    if np.array([car.Ch_constr[j] == -1 for car in cars]).astype(bool).any():
        for k, p in enumerate(cfg.p_work_charger_type):
            am.addConstr( # the product makes sure we only count work chargers
                sum([car.Yi[j][k] * (car.Ch_constr[j] == -1).astype(float)
                      for car in cars
                      ]) <= np.ceil(p*cfg.num_work_charger),
                name="C_numCh_" + str(j) + "_" + str(k),
                )
    else:
        continue



print("OK!")



#%% grid config

print("complex.py: ---------------------")
print("complex.py: Create grid object, variables and constraints",
      end='... ')


# costs for objective functions
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


# deal with net variables and bounds and objective coefficients
AdvancedNet.create_vars_obj(am)  # also generates objective coefficients

# deal with net constraint
AdvancedNet.create_nodal_constrs(am, cars, cars_data)


print("OK!")











#%% solve

print("complex.py: Solve the model...")
print("\n\ncomplex.py: ------------------\n\n")

am.optimize()


print("\n\ncomplex.py: ----------------\n\n")
















#######################################
#%% Post Proc Results
#######################################


#%% post process solution

print("complex.py: Post process Gurobi results back into Pandas frames",
      end='... ')

# temporary data for testing visualization
for i, car in enumerate(cars):
    # figure out which lines in the cars_data frame belong to car i
    car_bool = cars_data["CarId"] == i
    
    # add the charging load
    cars_data.loc[car_bool, "Load"] = np.array([Xtemp.X for Xtemp in car.Xi])
    cars_data.loc[car_bool, "Cap"] \
        = (car.P_chargers
                @ np.array(
                    [Ytemp.X for Yij in car.Yi for Ytemp in Yij])\
                        .reshape(cfg.K,
                                 len(car.P_chargers)
                                 ).T)
                        
    # cars_data.loc[car_bool, "Cap"]  = 11

for i, pp in enumerate(AdvancedNet.PPs):
    pp_bool = pp_data["PPId"] == i
    
    pp_data.loc[pp_bool, "Load"] = np.array([Xtemp.X for Xtemp in pp.P])

for i, l in enumerate(AdvancedNet.links):
    l_bool = grid_links["LinkId"] == i
    
    grid_links.loc[l_bool, "Load"] = np.array([Xtemp.X for Xtemp in l.Lp]) \
                                      - np.array([Xtemp.X for Xtemp in l.Lm])


print("OK!")



#%% plotting

if cartopy_exists:
    print("complex.py: Silently plot Cartopy maps",
      end='... ')
    
    outpath = "./plots/"
    fnamebase = "test"
    
    if cfg.grid_setting == -1:
        map_extent = [14.66, 14.76, 55.07, 55.135]; zoomlevel = 13; # Ronne
    else:
        map_extent = [14.65, 15.2, 54.97, 55.31]; zoomlevel = 10; # all of Bornholm 
    
    netplot = pt.netgif(map_extent, zoomlevel)  # Ronne
    netplot.plot_series(grid, grid_links, cars_data, pp_data, cons_data, outpath, fnamebase)
    
    plt.close("all")
    
    print("OK!")

print("complex.py: ------------------")
print("complex.py: MAIN PROGRAM DONE!")



#%% clean up

print("complex.py: Cleaning up workspace",
  end='... ')


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

print("OK!")

print("complex.py: FULLY DONE")
print("complex.py: ---------------")
print("complex.py: ---------------")







