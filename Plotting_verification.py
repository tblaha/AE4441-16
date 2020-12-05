# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 00:24:56 2020

@author: timon
"""

#Making some plot for verification 
from Lib.pp_gen import pp_data_base, pp_data
from Lib.cons_gen import cons_data_base, cons_data
from Lib import SimConfig as cfg
from Lib.grid_gen import grid_links
from Lib.cars_gen import cars_data

print(grid_links)

import numpy as np
import matplotlib.pyplot as plt

#Powerplant data 
power_plant_data = np.array(pp_data)
power_plant_names = power_plant_data[:,[1]]
power_plant_times = power_plant_data[:,[9]]
power_plant_capacities = power_plant_data[:,[10]]

consumer_data = np.array(cons_data)
consumer_names = consumer_data[:,[0]]
consumer_times = np.arange(0, cfg.K)
consumer_load = consumer_data[:,9]

#fig = plt.figure(figsize=(15,12)) #Defining size of plot 

#%%Plotting the powerplant capacities 

powerplants = False 
if powerplants == True: 
    #Actually plotting - Biomass 
    plt.subplot(2, 2, 1)
    plt.plot(power_plant_times[0:24],power_plant_capacities[0:24], label = power_plant_names[0][0])
    plt.title('Biomass Power Plant - Capacity')
    plt.xlabel('Time of day [h]')
    plt.ylabel('Power [kW]')
    plt.legend() 
    #plt.show()
    
    #Actually plotting - Wind
    plt.subplot(2, 2, 2)
    plt.plot(power_plant_times[0:23],power_plant_capacities[24:47], label = power_plant_names[24][0])
    plt.title('Wind Power - Capacity')
    plt.xlabel('Time of day [h]')
    plt.ylabel('Power [kW]')
    plt.legend() 
    #plt.show()
    
    #Actually plotting - Solar 
    plt.subplot(2, 2, 3)
    plt.plot(power_plant_times[0:23],power_plant_capacities[144:167], label = power_plant_names[144][0])
    plt.title('Solar Power - Capacity')
    plt.xlabel('Time of day [h]')
    plt.ylabel('Power [kW]')
    plt.legend() 
    #plt.show()
    
    #Actually plotting - Seacable
    plt.subplot(2, 2, 4)
    plt.plot(power_plant_times[0:23],power_plant_capacities[192:215], label = power_plant_names[192][0])
    plt.title('Seacable Power - Capacity ')
    plt.xlabel('Time of day [h]')
    plt.ylabel('Power [kW]')
    plt.legend() 
    plt.show()

#%%Plotting the consumers 

consumers = False    
if consumers == True: 
    #Actually plotting - the first consumer 
    values = cons_data.groupby("Time")["Load"].sum()
    plt.plot(consumer_times, values)
    plt.hlines(y=30000,xmin = 0,xmax = 24, color='g', linestyle='--', label = 'Mean')
    plt.hlines(y=38000,xmin = 0,xmax = 24, color='r', linestyle='-', label = 'Peak')
    plt.title('Consumer Demand Over timeslots')
    plt.xlabel('Time of day [h]')
    plt.ylabel('Power [kW]')
    plt.legend()
    plt.show()


#%%Plotting the grid verification 
fig4, ax4 = plt.subplots(1,1,figsize=(10, 6))
grid = True 
if grid == True: 
    ax4.hist(grid_links["Load"],
         # [cars[i].s_day for i in range(len(cars))],
         bins=35,
         density=True,
         cumulative=False,
         histtype='step',
         color="blue",
         lw=2,
         )
    
plt.legend(loc="lower right", fontsize=14)    
ax4.set_xlabel("Grid Laods", fontsize=16)
ax4.set_ylabel("Cumulative Distribution", fontsize=16)
plt.show()


    
  
    
    


