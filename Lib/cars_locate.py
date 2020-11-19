#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:14:59 2020

@author: tblaha
"""

#% reset python workspace
from IPython import get_ipython
get_ipython().magic('reset -sf')

import pandas as pd
import numpy as np
from numpy import random as npr
npr.seed(1)
import random
from Lib import cars as crs
from Lib import SimConfig as cfg
Re=6731000

# generate grid connection and location
grid = pd.DataFrame(columns=["Long", "Lat", "Radius", "Type", "Color", "Size"])
grid = grid.astype({"Long": float, 
                    "Lat": float, 
                    "Radius": float,
                    "Type": str, 
                    "Color": str, 
                    "Size": float,
                    })
grid.loc["Ronne"] = [14.7110, 55.0966, 3000, "60kV Station", "Orange", 50]
grid.loc["Nexo"]  = [15.1291, 55.0585, 3000, "60kV Station", "Orange", 50]
grid.loc["Tejn"]  = [14.8360, 55.2474, 3000, "60kV Station", "Orange", 50]

C = len(grid)


# Repeat entries such that we have one per time slot per car
crs.cars_data = crs.cars_data.loc[
    crs.cars_data.index.repeat(cfg.K)
    ].reset_index(drop=True)


car_dist  = [2, 2, 1]
car_alloc = [k for k in range(C) for l in range(car_dist[k])]
npr.shuffle(car_alloc)

for i, c in enumerate(car_alloc):
    car_bool = crs.cars_data["CarId"] == i
    
    grid_idxes = grid.index[car_alloc[i]]
    
    crs.cars_data.loc[car_bool, "GridNode"] \
        = grid_idxes
        
    rad = grid.loc[grid_idxes, "Radius"]
    long = grid.loc[grid_idxes, "Long"]
    lat = grid.loc[grid_idxes, "Lat"]
    mu = np.array([long, lat])
    
    sx, sy = rad/2 / np.array([Re/360 * np.cos(lat*np.pi/180), 
                               Re/360])
    cov = np.diag(np.array([sx, sy])**2)
    
    crs.cars_data.loc[car_bool, ["Long", "Lat"]]\
        = npr.multivariate_normal(mu, cov, size=1)[0]
    
    crs.cars_data.loc[car_bool, ["time"]] = np.arange(cfg.K).astype(int)
    crs.cars_data.loc[car_bool, ["Charger type"]] = 1
    


# car_switch_probability = 0.5

# random_ids = npr.shuffle(crs.cars_data.loc[:, "CarId"])
