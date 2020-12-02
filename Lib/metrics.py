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
    fig, axs = plt.subplots(1, 1, constrained_layout=True, figsize=(9, 7))
    
    
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

    #%% make annotation
    cons_total = cfg.dt @ cons_loads * 1e-3
    cars_total = cfg.dt @ cars_loads * 1e-3
    gross_imports_EVs = (cfg.dt[pp_np[0, :] > 0] 
                             @ pp_np[0, pp_np[0, :] > 0]
                             ).sum() * 1e-3
    
    gross_imports_noEVs = (cfg.dt[pp_np[1:, :].sum(axis=0) <= cons_loads]
                           @ (cons_loads[pp_np[1:, :].sum(axis=0) <= cons_loads]
                                -  pp_np[1:, pp_np[1:, :].sum(axis=0) <= cons_loads].sum(axis=0)
                                )) * 1e-3
    
    
    textstr = '\n'.join((
        r'#EVs = %d          ' % (len(cars), ),
        r'Consumtion w/o EVs = %4.0f MWh' % (cons_total, ),
        r'Consumtion w EVs = %4.0f MWh' % (cars_total + cons_total, ),
        r'Cable imports w/o EVs = %3.1f MWh' % (gross_imports_noEVs, ),
        r'Cable imports w EVs = %5.1f MWh' % (gross_imports_EVs, ),
        ))
    
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    axs.text(0.975, 0.975, textstr, transform=axs.transAxes, fontsize=14,
             verticalalignment='top', ha='right', bbox=props)

    #%% make plot pretty
    
    axs.grid()
    axs.set_xlim(left=0, right=24)
    axs.set_ylim(top=5.5e4)
    axs.set_ylabel("Power [kW]", fontsize = 16)
    axs.set_xlabel("Time of Day [h]", fontsize = 16)
    axs.legend(loc="upper left", fontsize = 12)
    axs.ticklabel_format(axis="y", style="sci", scilimits=(3,3))
    
    
    #%% save and return
    
    plt.savefig("./plots/PowerHourly.eps")


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


def charger_pie(cars_data):
    from matplotlib.ticker import FuncFormatter
    
    plt.close("all")
    fig, ax = plt.subplots(1, 1, constrained_layout=True, figsize=(6, 6))
    # ax.grid()
    # ax.set_xlim(left=0, right=24)
    # ax.set_xlabel("Time of Day [h]", fontsize=16)
    # ax.set_ylabel("Charging Power [kW], + charge, - discharge", fontsize=16)
    
    #ax.set_ylim(top=load_max*1.5)
    home_charger_choice = cars_data.groupby("CarId").first()\
                                   .groupby("Actual Charger Type").size()*1e-3
    
    gross_home_charger_load \
        = cars_data.loc[cars_data["Charger type"] > 0, :]\
            .groupby("Charger type")["Load"].apply(lambda x: sum(abs(x)))*1e-3
            
    work_charger_choice \
        = cars_data.loc[cars_data["Charger type"] == -1, :]\
            .groupby(["Time", "Actual Charger Type"]).size()\
            .groupby("Actual Charger Type").max()*1e-3
    
    gross_work_charger_load \
        = cars_data.loc[cars_data["Charger type"] == -1, :]\
            .groupby("Actual Charger Type")["Load"]\
                .apply(lambda x: sum(abs(x)))*1e-3
    
    # going by car objects:
    # b = np.array([max([sum([cars[i].Yi[j][k].X for i in range(len(cars))]) for j in range(6, 18)]) for k in range(4)])
    
    # Compute pie slices
    amount = np.zeros(len(home_charger_choice) + len(work_charger_choice)-1)
    amount[:len(home_charger_choice)] = home_charger_choice.to_numpy()
    amount[len(home_charger_choice):] = work_charger_choice.loc[1:].to_numpy()
    
    width = 2*np.pi * amount/sum(amount)
    theta = np.zeros_like(width)
    theta[0] = 0
    theta[1:] = np.cumsum(width)[:-1]
    
    radii = np.zeros_like(width)
    radii[:len(home_charger_choice)] = gross_home_charger_load
    radii[len(home_charger_choice):] = gross_work_charger_load[:-1]
    radii = np.log10(radii / amount)
    
    colors = plt.cm.jet(np.linspace(0, 1, len(amount)))
    
    ax = plt.subplot(111, projection='polar')
    j=0
    for i,r in home_charger_choice.iteritems():
        ax.bar(theta[j]+width[j]/2, radii[j], width=width[j], bottom=0.0, color=colors[j],
                   label="Home: Type "+str(i))
        j+=1
        
    for i,r in work_charger_choice.iteritems():
        if i > 0:
            ax.bar(theta[j]+width[j]/2, radii[j], width=width[j], bottom=0.0, color=colors[j],
                   label="Work: Type "+str(i))
            j+=1
    
    
    rad2fmt = lambda x,pos: f"{x/(2*np.pi) * 100:.0f}%"
    exp2fmt = lambda x,pos: f"$10^{{{x:.1f}}}$"
    ax.xaxis.set_major_formatter(FuncFormatter(rad2fmt))
    ax.yaxis.set_major_formatter(FuncFormatter(exp2fmt))
    ax.set_rlim(bottom=0, top=max(radii))
    ax.set_rlabel_position(150)
    
    ax.text(np.radians(160),ax.get_rmax()*0.6,'Mean Throughput\nper Charger [kWh]',
        rotation=-20,ha='center',va='center', fontsize=14)
    ax.text(np.radians(45),ax.get_rmax()*1.2,'Share of Chargers',
        rotation=-45,ha='center',va='center', fontsize=14)
    
    #ax.tick_params(label=True)
    ax.tick_params(axis="y", labelsize=14)
    
    ax.legend(loc="lower right", bbox_to_anchor=(1.1, -0.1), fontsize=12)


    
    #ax.legend(loc="upper left", fontsize=12)
