#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:41:26 2020

@author: tblaha
"""

import pandas as pd
import numpy as np
from Lib import SimConfig as cfg


#%% grid data frames

# generate grid connection and location
grid = pd.DataFrame(columns=["Long", 
                             "Lat",
                             "2SigRadius", # 95.7% radius of cars spread
                             "Type",       # what type of power sustation
                             "Color",      # for plotting
                             "Size",       # for plotting
                             ])
grid = grid.astype({"Long": float, 
                    "Lat": float, 
                    "2SigRadius": float,
                    "Type": str, 
                    "Color": str, 
                    "Size": float,
                    })

# grid links data frame
grid_links_base = pd.DataFrame(columns=["LinkId",
                                       "conn1", # first connection
                                       "conn2", # second connection
                                       "Cap",   # capacity of link
                                       ])

grid_links_base = grid_links_base.astype({"LinkId": int,
                                        "conn1": str, # first connection
                                        "conn2": str, # second connection
                                        "Cap": float,   # capacity of link kW
                                        })


if cfg.grid_setting == 1:
    grid.loc["Ronne"] = [14.713889, 55.097778, 1500, "60kV Station", "Pink", 200]
    grid_links_base["LinkId"] = grid_links_base.index

elif cfg.grid_setting == 3:
    grid.loc["Ronne"] = [14.713889, 55.097778, 1500, "60kV Station", "Pink", 200]
    grid.loc["Nexo"]  = [15.1291, 55.0585, 1500, "60kV Station", "Pink", 200]
    grid.loc["Tejn"]  = [14.8360, 55.2474, 1500, "60kV Station", "Pink", 200]
    
    grid_links_base.loc[0, ["conn1", "conn2", "Cap"]] = ["Ronne", "Nexo", 100000]
    grid_links_base.loc[1, ["conn1", "conn2", "Cap"]] = ["Ronne", "Tejn", 100000]
    grid_links_base.loc[2, ["conn1", "conn2", "Cap"]] = ["Nexo",  "Tejn", 100000]
    
    grid_links_base["LinkId"] = grid_links_base.index
    
elif cfg.grid_setting == -1:
    grid.loc["Akirkeby"]     = [14.897778, 55.068056, 1500, "60kV", "Pink", 200]
    grid.loc["Allinge"]      = [14.800278, 55.268333, 1500, "60kV", "Pink", 200]
    grid.loc["Bodilsker"]    = [15.065833, 55.063056, 1500, "60kV", "Pink", 200]
    grid.loc["Dalslunde"]    = [15.050833, 55.100000, 1500, "60kV", "Pink", 200]
    grid.loc["Gudhjem"]      = [14.953056, 55.199167, 1500, "60kV", "Pink", 200]
    grid.loc["Hasle"]        = [14.723333, 55.170278, 1500, "60kV", "Pink", 200]
    grid.loc["Nexo"]         = [15.115833, 55.063056, 1500, "60kV", "Pink", 200]
    grid.loc["Olsker"]       = [14.795556, 55.231944, 1500, "60kV", "Pink", 200]
    grid.loc["Osterlars"]    = [14.935000, 55.153333, 1500, "60kV", "Pink", 200]
    grid.loc["Poulsker"]     = [15.055833, 55.022222, 1500, "60kV", "Pink", 200]
    grid.loc["Ronne"]        = [14.713889, 55.097778, 1500, "60kV", "Pink", 200]
    grid.loc["Ronne Nord"]   = [14.707778, 55.111111, 1500, "60kV", "Pink", 200]
    grid.loc["Ronne Syd"]    = [14.730556, 55.089722, 1500, "60kV", "Pink", 200]
    grid.loc["Snorrebakken"] = [14.744444, 55.111667, 1500, "60kV", "Pink", 200]
    grid.loc["Svaneke"]      = [15.136111, 55.134722, 1500, "60kV", "Pink", 200]
    grid.loc["Vesthavnen"]   = [14.690556, 55.102778, 1500, "60kV", "Pink", 200]
    
    grid_links_base.loc[0] = [0, "Ronne", "Ronne Syd", 10000]
    grid_links_base.loc[1] = [1, "Ronne", "Ronne Nord", 10000]
    grid_links_base.loc[2] = [2, "Ronne", "Vesthavnen", 10000]
    grid_links_base.loc[3] = [3, "Ronne", "Snorrebakken", 10000]
    grid_links_base.loc[4] = [4, "Ronne Nord", "Hasle", 10000]
    grid_links_base.loc[5] = [5, "Snorrebakken", "Hasle", 10000]
    grid_links_base.loc[6] = [6, "Ronne Syd", "Akirkeby", 10000]
    grid_links_base.loc[7] = [7, "Akirkeby", "Bodilsker", 10000]
    grid_links_base.loc[8] = [8, "Bodilsker", "Poulsker", 10000]
    grid_links_base.loc[9] = [9, "Bodilsker", "Nexo", 10000]
    grid_links_base.loc[10] = [10, "Nexo", "Svaneke", 10000]
    grid_links_base.loc[11] = [11, "Dalslunde", "Bodilsker", 10000]
    grid_links_base.loc[12] = [12, "Dalslunde", "Svaneke", 10000]
    grid_links_base.loc[13] = [13, "Dalslunde", "Osterlars", 10000]
    grid_links_base.loc[14] = [14, "Hasle", "Olsker", 10000]
    grid_links_base.loc[15] = [15, "Olsker", "Allinge", 10000]
    grid_links_base.loc[16] = [16, "Olsker", "Osterlars", 10000]
    grid_links_base.loc[17] = [17, "Osterlars", "Gudhjem", 10000]








#%% grid links data --> time-dependent

# Repeat entries such that we have one per time slot per powerplant
grid_links = grid_links_base.loc[
    grid_links_base.index.repeat(cfg.K)
    ].reset_index(drop=True)

grid_links["Time"] = np.tile(np.arange(cfg.K), len(grid_links_base)).astype(int)
grid_links["Load"] = 0.














