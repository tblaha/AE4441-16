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


def _make_annot(cars, cars_data, cars_bool, load_max, axs, car_id):
    
    #%% Figure out charger types
            
    ct = cars_data.loc[cars_bool, "Charger type"].to_numpy()
    cp = cars_data.loc[cars_bool, "Charger Power"].to_numpy()
    r = np.arange(cfg.K)
    first_non_home = r[ct != ct[0]][0]
    last_non_home  = r[ct != ct[0]][-1]
    charger_work_power = max(cp[ct == -1])
    
    
    #%% make textbox
    textstr = '\n'.join((
r'Car Id = %s' % (cars[car_id].name, ),
r'Car Type = %s' % (cars_data.loc[cars_bool, "Car Type"].iat[0], ),
r'Homecharger Capacity = %d kW' % (cars_data.loc[cars_bool, "Charger Power"].iat[0], ),
r'Workcharger Capacity = %d kW' % (charger_work_power, ),
r'Net Energy = %.2f kWh' % (cfg.dt[0] * sum(cars_data.loc[cars_bool, "Load"])
                               , ),
r'Driven Energy = %.2f kWh' % (
cars_data.loc[cars_bool, "Distance Driven"].iat[0]
* cars_data.loc[cars_bool, "kWh/km"].iat[0], ),
))
    
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    axs.text(0.05, 0.325, textstr, transform=axs.transAxes, fontsize=16,
             verticalalignment='top', bbox=props)
    
    
    #%% make arrows
    
    y_coord = load_max*1.2
    
    aprops=dict(arrowstyle='<->', mutation_scale=20)
    xy_s = [cfg.t[0],
            cfg.t[first_non_home-1],
            cfg.t[last_non_home],
            cfg.t[-1]
            ]
    texts = ["Home", "Work", "Home"]
    for i in range(len(xy_s)-1):
        axs.annotate(text='',
                     xytext=(xy_s[i],y_coord),
                     xy=(xy_s[i+1],y_coord),
                     arrowprops=aprops,
                     )
        axs.annotate(text=texts[i],
                     xy=(0,0),
                     xytext=(0.5*xy_s[i]+0.5*xy_s[i+1],
                             y_coord*1.075),
                     ha='center',
                     fontsize=14,
                     )
    
    return axs


def car_plot_bar(cars, cars_data, car_ids, make_annot=False):
    
    plt.close("all")
    fig, axs = plt.subplots(1, 1, constrained_layout=True, figsize=(9, 6))
    beun = cfg.dt[0]*(0.9/len(car_ids))
    
    load_max = 0
    for i, car_id in enumerate(car_ids):
        cars_bool = cars_data["CarId"] == car_id
        
        car_load = cars_data.loc[cars_bool, "Load"]
        
        axs.bar(cfg.t+i*beun - beun, car_load, width=beun,
                label="EV"+cars[car_id].name)
        
        load_max = max(load_max, np.max(car_load))
        
        if (i == 0) and make_annot:
            axs = _make_annot(cars, cars_data, cars_bool, load_max, axs, car_id)
    
    axs.grid()
    axs.set_xlim(left=0, right=24)
    axs.set_xlabel("Time of Day [h]", fontsize=16)
    axs.set_ylabel("Charging Power [kW], + charge, - discharge", fontsize=16)
    axs.set_ylim(top=load_max*1.5)
    if not make_annot:
        axs.legend(loc="upper left", fontsize=12)
    
    
def car_plot_line(cars, cars_data, car_ids, make_annot=False):
    
    plt.close("all")
    fig, axs = plt.subplots(1, 1, constrained_layout=True, figsize=(9, 6))
    
    load_max = 0
    markers = ["x", "s", "*", "+", "o", "^", "1", "p", "D"]
    for i, car_id in enumerate(car_ids):
        cars_bool = cars_data["CarId"] == car_id
        
        car_load = cars_data.loc[cars_bool, "Load"]
        
        axs.plot(cfg.t, car_load,
                 lw=2, ls="-", markersize=9, marker=markers[i],
                 label="EV"+cars[car_id].name
                 )
        
        load_max = max(load_max, np.max(car_load))
        
        if (i == 0) and make_annot:
            axs = _make_annot(cars, cars_data, cars_bool, load_max, axs, car_id)
    
    axs.grid()
    axs.set_xlim(left=0, right=24)
    axs.set_xlabel("Time of Day [h]", fontsize=16)
    axs.set_ylabel("Charging Power [kW], + charge, - discharge", fontsize=16)
    axs.set_ylim(top=load_max*1.5)
    
    if not make_annot:
        axs.legend(loc="upper left", fontsize=12)
