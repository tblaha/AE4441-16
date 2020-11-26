#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:32:46 2020

@author: tblaha
"""
import pandas as pd

from Lib import SimConfig as cfg
from Lib.pp_gen import pp_data
from Lib.cons_gen import cons_data
from matplotlib import pyplot as plt

plt.close("all")
fig, axs = plt.subplots(2, 1, constrained_layout=True, figsize=(8, 8))


#%% verify Power Plant Capacities


power_sums = pp_data.groupby(["Type", "Time"])["Cap"].sum()

for key, val in cfg.max_caps.items():
    axs[0].plot(cfg.t, power_sums.loc[key], label=key)
    
# plot sustainable sum
sus_sum = pp_data.groupby(["Sustainability", "Time"])["Cap"].sum()
axs[0].plot(cfg.t, sus_sum["sustainable"],
            label="Sustainable Capacity", linestyle="--")

# plot total power available
axs[0].plot(cfg.t, sus_sum.groupby("Time").sum(),
            label="Total Capacity", linestyle="--")

    
axs[0].legend(fontsize=9, loc="upper right")

axs[0].grid()
axs[0].set_xlim(left=0, right=24)
axs[0].set_ylim(bottom=0)
axs[0].set_title("Aggregated Powerplant capacities by type", fontsize=18)
axs[0].set_ylabel("Powerplant Capacity [kW]", fontsize=16)


#%% verify Consumer Demands


# plot consumer sum
cons_sums = cons_data.groupby(["Time"])["Load"].sum()
axs[1].plot(cfg.t, cons_sums, label="Total Consumer Demand", linestyle="-")

# per consumer
# for gridnode in pd.unique(cons_data["GridConn"]):
#     axs[1].plot(cfg.t, 
#                 cons_data.loc[cons_data["GridConn"] == gridnode, "Load"],
#                 label=gridnode,
#                 )

# overlay available power:
axs[1].plot(cfg.t, sus_sum["sustainable"],
            label="Sustainable Capacity", linestyle="-.")
axs[1].plot(cfg.t, sus_sum.groupby("Time").sum(),
            label="Total Capacity", linestyle="-.")


axs[1].legend(fontsize=9)

axs[1].grid()
axs[1].set_xlim(left=0, right=24)
axs[1].set_ylim(bottom=0)
axs[1].set_title("Consumer Demand", fontsize=18)
axs[1].set_xlabel("Time of Day [h]", fontsize=16)
axs[1].set_ylabel("Consumer Demand [kW]", fontsize=16)