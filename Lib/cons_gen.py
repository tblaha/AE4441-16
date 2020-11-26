#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:04:13 2020

@author: tblaha
"""

import numpy as np
import pandas as pd
from Lib.grid_gen import grid

# import the global config
from Lib import SimConfig as cfg


#%% consumer data frame --> time independent data

cons_data_base = pd.DataFrame(columns=["ConsId",
                                       "Long",
                                       "Lat",
                                       "GridConn",
                                       "Color",
                                       "RelCons",
                                       "Size",
                                       "Peak",
                                       ])

i = 0
for index, row in grid.iterrows():
    gc_loc = row[["Long", "Lat"]].to_numpy()
    centre_vector = (np.array([14.9291, 55.1146]) - gc_loc)
    dem_loc = gc_loc + 0.025*centre_vector / np.linalg.norm(centre_vector)
    
    cons_data_base.loc[index, ["Long", "Lat"]] = dem_loc
    cons_data_base.loc[index, "GridConn"] = index
    cons_data_base.loc[index, ["Color", "Size"]] = ["Purple", 300]
    cons_data_base.loc[index, "RelCons"] = cfg.rel_cons_distribution[i]
    
    # beeeeeeuuuun
    i += 1

# normalize Relative Consumption

cons_data_base["RelCons"] = cons_data_base["RelCons"] \
                            / cons_data_base["RelCons"].sum()
                            
# peak consumption
cons_data_base["Peak"] = cfg.cons_peak * cons_data_base["RelCons"]

# index column
cons_data_base["ConsId"] = cons_data_base.index

# apply dtypes
cons_data_base = cons_data_base.astype({"ConsId": str,
                                        "Long": float, 
                                        "Lat": float,
                                        "GridConn": str,
                                        "Color": str,
                                        "RelCons": float, 
                                        "Size": float, 
                                        "Peak": float,
                                        })



#%% consumer data frame --> time dependent data

# implement quad-linear demand curve
# https://www.eia.gov/todayinenergy/detail.php?id=830
def tot_cons(t, avg, peak):
    ni = (24 * avg - 5/2 * peak) / 29.5 # night power
    if (t >= 0) & (t < 6):
        return ni
    elif (t >= 6) & (t < 9):
        return ni * (1 + 1/2 * (t - 6)/3)
    elif (t >= 9) & (t < 19):
        return ni * 3/2
    elif (t >= 19) & (t < 24):
        return peak - (peak - ni) * (t - 19)/5
    else:
        raise("t outside 0-24h interval")

# total consumer demand for each time slot
tot_cons_dem = np.array([tot_cons(t, cfg.cons_mean, cfg.cons_peak) 
                         for t in cfg.t
                         ])

# Repeat entries such that we have one per time slot per powerplant
cons_data = cons_data_base.loc[
    cons_data_base.index.repeat(cfg.K)
    ].reset_index(drop=True)


for index, row in grid.iterrows():
    # assign values for each group of ppl at the grid nodes
    cons_bool = cons_data["GridConn"] == index
    local_cons = cons_data.loc[cons_bool, "RelCons"].iat[0]
    
    cons_data.loc[cons_bool, "Time"] = np.arange(cfg.K).astype(int)
    cons_data.loc[cons_bool, "Load"] = local_cons * tot_cons_dem
    
    
cons_data = cons_data.astype({"Time": int,
                              "Load": float,
                              })


        