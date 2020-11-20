#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:32:46 2020

@author: tblaha
"""
import pandas as pd

from Lib import SimConfig as cfg
from Lib.grid import pp_data, cons_data
from matplotlib import pyplot as plt

plt.close("all")
fig, axs = plt.subplots(2, 1, constrained_layout=True, figsize=(8,8))


#%% verify Power Plant Capacities


power_sums = pp_data.groupby(["Type", "Time"])["Cap"].sum()

for key, val in cfg.max_caps.items():
    axs[0].plot(cfg.t, power_sums.loc[key], label=key)
    
axs[0].legend(fontsize=12, loc="upper right")

axs[0].grid()
axs[0].set_title("Aggregated Powerplant capacities by type", fontsize=18)
axs[0].set_ylabel("Powerplant capacity [kW]", fontsize=16)


#%% verify Consumer Demands


for gridnode in pd.unique(cons_data["GridConn"]):
    axs[1].plot(cfg.t, 
                cons_data.loc[cons_data["GridConn"] == gridnode, "Load"],
                label=gridnode,
                )

cons_sums = cons_data.groupby(["Time"])["Load"].sum()
axs[1].plot(cfg.t, cons_sums, label="Consumer Demand")

axs[1].legend(fontsize=12)

axs[1].grid()
axs[1].set_title("Aggregated Consumer Demand", fontsize=18)
axs[1].set_xlabel("Time of Day [h]", fontsize=16)
axs[1].set_ylabel("Consumer Demand [kW]", fontsize=16)