#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:27:29 2020

@author: tblaha
"""

import numpy as np
from Lib import SimConfig as cfg
from matplotlib import pyplot as plt

def power_plot(cars, cars_data, AdvancedNet, pp_data, grid_links, cons_data):
    
    #%% prepare data
    # get pp loads per pp-type using very simple elementary pandas that I for 
    # sure did not have to google for for 30minutes
    pp_loads = pp_data\
        .sort_values(["Sustainability", "Type", "Time"],
                     ascending=(False, True, True),
                     )\
        .groupby(["Type", "Time"], sort=False)["Load"].sum()\
            .unstack(level=0)
            
    cons_loads = cons_data.groupby("Time")["Load"].sum()
    cars_loads = cars_data.groupby("Time")["Load"].sum()
    
    # convert to numpy for plotting
    pp_np = pp_loads.to_numpy().T
    
    # make figure
    plt.close("all")
    fig, axs = plt.subplots(1, 1, constrained_layout=True, figsize=(9, 6))
    
    
    #%% plot stacks
    
    # basic sustainable stack-plot
    stacks = axs.stackplot(cfg.t, pp_np[1:, :],
                           lw=1, linestyle="-",
                           colors=["Brown", "Orange", "White"],
                           labels=pp_loads.columns[1:],
                           )
    hatches=["\\", "//","x"]
    for stack, hatch in zip(stacks, hatches):
        stack.set_hatch(hatch)
        
    # show top of stackplot with a thin line
    axs.plot(cfg.t, pp_np[1:, :].sum(axis=0), c="k", lw=1)

    # plot consumers and consumers + EVs
    axs.plot(cfg.t, cons_loads,
                color='purple', lw=4, ls="-", label="Domestic Load")
    
    axs.plot(cfg.t, cars_loads + cons_loads,
                color='blue', lw=4, ls="--", label="Domestic Load + EVs")
    
    # plot net import by cable as a stack plot around the 0 axis
    net_stack = axs.stackplot(cfg.t, pp_np[0, :], colors=["black"],
                                 labels=["Net Import by Cable"])
    net_stack[0].set_hatch(".")
    net_stack[0].set_edgecolor("white")


    #%% make plot pretty
    
    axs.grid()
    axs.set_xlim(left=0, right=24)
    axs.set_ylim(top=5e4)
    axs.set_ylabel("Power [kW]", fontsize = 16)
    axs.set_xlabel("Time of Day [h]", fontsize = 16)
    axs.legend(loc="upper left", fontsize = 10)
    axs.ticklabel_format(axis="y", style="sci", scilimits=(3,3))
    
    
    #%% save and return
    
    plt.savefig("./plots/PowerHourly.eps")
    
    return fig

