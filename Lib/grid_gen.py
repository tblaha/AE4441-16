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
    grid.loc["Ronne"] = [14.7110, 55.0966, 1500, "60kV Station", "Orange", 200]
    grid_links_base["LinkId"] = grid_links_base.index

elif cfg.grid_setting == 3:
    grid.loc["Ronne"] = [14.7110, 55.0966, 1500, "60kV Station", "Orange", 200]
    grid.loc["Nexo"]  = [15.1291, 55.0585, 1500, "60kV Station", "Orange", 200]
    grid.loc["Tejn"]  = [14.8360, 55.2474, 1500, "60kV Station", "Orange", 200]
    
    grid_links_base.loc[0, ["conn1", "conn2", "Cap"]] = ["Ronne", "Nexo", 100000]
    grid_links_base.loc[1, ["conn1", "conn2", "Cap"]] = ["Ronne", "Tejn", 100000]
    grid_links_base.loc[2, ["conn1", "conn2", "Cap"]] = ["Nexo",  "Tejn", 100000]
    
    grid_links_base["LinkId"] = grid_links_base.index
elif cfg.grid_setting == -1:
    pass













#%% grid links data frame --> time independent base








#%% grid links data --> time-dependent

# Repeat entries such that we have one per time slot per powerplant
grid_links = grid_links_base.loc[
    grid_links_base.index.repeat(cfg.K)
    ].reset_index(drop=True)

grid_links["Time"] = np.tile(np.arange(cfg.K), len(grid_links_base)).astype(int)
grid_links["Load"] = 0.














