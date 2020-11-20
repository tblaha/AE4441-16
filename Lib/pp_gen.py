#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:03:16 2020

@author: tblaha
"""

import numpy as np
import pandas as pd
import copy

# import the global config
from Lib import SimConfig as cfg


#%% powerplant data frame --> timeslot-independent attributes

pp_data_base = pd.DataFrame(columns=["Name",
                                     "Long", 
                                     "Lat",
                                     "Type",
                                     "Sustainability",
                                     "GridConn",
                                     "Color",
                                     "Size",
                                     ])

pp_data_base.loc["Biomass"]    = ["Biomass",    14.6963, 55.0938, "Biomass", 
                                  "sustainable", "Ronne", "Brown", 30]

pp_data_base.loc["WindWest"]   = ["WindWest",   14.7491, 55.0809, "Wind",
                                  "sustainable", "Ronne", "White", 30]

pp_data_base.loc["WindNorth"]  = ["WindNorth",  14.7564, 55.2552, "Wind",
                                  "sustainable", "Tejn",  "White", 30]

pp_data_base.loc["WindEast"]   = ["WindEast",   15.0928, 55.0815, "Wind",
                                  "sustainable", "Nexo",  "White", 30]

pp_data_base.loc["SolarWest"]  = ["SolarWest",  14.7241, 55.1312, "Solar",
                                  "sustainable", "Ronne", "Orange", 30]

pp_data_base.loc["SolarNorth"] = ["SolarNorth", 14.8539, 55.2314, "Solar",
                                  "sustainable", "Tejn",  "Orange", 30]

pp_data_base.loc["SolarEast"]  = ["SolarEast",  15.0877, 55.0408, "Solar",
                                  "sustainable", "Nexo",  "Orange", 30]

pp_data_base.loc["Cable"]      = ["Cable",      14.6898, 55.1884, "Cable",
                                  "unsustainable", "Ronne", "Black", 30]

pp_data_base = pp_data_base.astype({"Name": str,
                                    "Long": float, 
                                    "Lat": float,
                                    "Type": str,
                                    "Sustainability": str,
                                    "GridConn": str,
                                    "Color": str,
                                    "Size": float, 
                                    })


#%% powerplant data frame --> timeslot-dependent attributes

# figure out how many pwoer plants we have per type (wind, solar...)
pp_num = copy.deepcopy(cfg.max_caps)
for key, val in cfg.max_caps.items():
    pp_num[key] = sum(pp_data_base["Type"] == key)
    
# Repeat entries such that we have one per time slot per powerplant
pp_data = pp_data_base.loc[
    pp_data_base.index.repeat(cfg.K)
    ].reset_index(drop=True)


# capacity time distribution
lambda_sol = np.cos(2*np.pi/24 * (12 - cfg.dtday/2 ))  # cosine adjustment to guarantee daylight hours
cap_distr = {"Biomass": np.ones(cfg.K),
             "Wind": 1 + 0.25 * np.sin(2*np.pi/24 * cfg.t),
             "Solar": np.maximum(0, lambda_sol - np.cos(2*np.pi/24 * cfg.t)),
             "Cable": np.ones(cfg.K),
             }

for key, val in cfg.max_caps.items():
    pp_bool = pp_data["Type"] == key
    
    pp_data.loc[pp_bool, "Time"] = np.tile(np.arange(cfg.K), pp_num[key])
    pp_data.loc[pp_bool, "Cap"] = (
        cfg.max_caps[key] # max capacity 
        * np.tile(cap_distr[key] / np.max(cap_distr[key]), # normalized rel cap
                  pp_num[key]) # repeated for how many plants we have
        / pp_num[key])  # since cfg.max_caps is the overall cap; devide by 
                        # number of plants for this type of energy

    pp_data.loc[pp_bool, "Load"] = 0.0

pp_data = pp_data.astype({"Time": int,                                  "Time": int,
                          "Cap": float,
                          "Load": float,
                          })
