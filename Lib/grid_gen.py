#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:41:26 2020

@author: tblaha
"""

import pandas as pd
import numpy as np
from Lib import SimConfig as cfg


#%% grid data frame

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

grid.loc["Ronne"] = [14.7110, 55.0966, 3000, "60kV Station", "Orange", 50]
grid.loc["Nexo"]  = [15.1291, 55.0585, 3000, "60kV Station", "Orange", 50]
grid.loc["Tejn"]  = [14.8360, 55.2474, 3000, "60kV Station", "Orange", 50]


#%% grid links data frame --> time independent base

grid_link_base = pd.DataFrame(columns=["LinkId",
                                       "conn1", # first connection
                                       "conn2", # second connection
                                       "Cap",   # capacity of link
                                       ])

grid_link_base = grid_link_base.astype({"LinkId": int,
                                        "conn1": str, # first connection
                                        "conn2": str, # second connection
                                        "Cap": float,   # capacity of link kW
                                        })

grid_link_base.loc[0, ["conn1", "conn2", "Cap"]] = ["Ronne", "Nexo", 10000]
grid_link_base.loc[1, ["conn1", "conn2", "Cap"]] = ["Ronne", "Tejn", 10000]
grid_link_base.loc[2, ["conn1", "conn2", "Cap"]] = ["Nexo",  "Tejn", 10000]

grid_link_base["LinkId"] = grid_link_base.index

#%% grid links data --> time-dependent

# Repeat entries such that we have one per time slot per powerplant
grid_link = grid_link_base.loc[
    grid_link_base.index.repeat(cfg.K)
    ].reset_index(drop=True)

grid_link["Time"] = np.tile(np.arange(cfg.K), len(grid_link_base)).astype(int)
grid_link["Load"] = 0.














