# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:32:53 2020

@author: timon
"""
#Better estimation of power through sustainable sources: Solar & Wind 
#Coordinates Bornholm = 55°07'39.5"N 14°54'59.4"E

#What does the program do?: 
    
""" Program takes as an input: Total sustainable power in GWh 
            Program gives as an output: More realistic distribution 
            the sustainable power during any given day. """

#%% Importing some stuff & defining variables that are used later on

import numpy as np 
import pandas as pd 
import os

from Lib import SimConfig as cfg

E_daily = 287000/365.           # Total yearly energy demand is 287000 [MWh] (ref. 2012)
fraction_sust = 0.75            # Fraction of energy that is sustainable (assumption)

E_daily_sust = E_daily*fraction_sust            #Energy demand met with sustainable source [MWh] 
E_daily_unsust = E_daily*(1.0-fraction_sust)    #Energy demand met with unsustainable source [MWh]

w_solar = 0.2                   # 20 percent of sustainable power is solar in 2050 
w_wind = (1.0 - w_solar)        # 80 percent of sustainable power is wind (or other) in 2050


#%% Reading solar irradiance from excel file solar_rad.xlsx & making numpy array (solardata) 

cwd = os.getcwd()       

#This excel file is for the 31st of March at lattitude 55 (Bornholm)
#From site https://www.pveducation.org/pvcdrom/properties-of-sunlight/calculation-of-solar-insolation
#Concerns the average solar irradiation at that lattitude [kW/m2]
instance_name = 'Solar_rad.xlsx' #Importing excel file with solar irradiance 

#Excel -> pandas dataframe -> numpy array 
df = pd.read_excel(os.path.join(cwd,instance_name)) 
array = df.values 
solardata = np.array(array)


#%


#%% Similar for the wind power (windpower_frac), assumed to be constant 
# throuhgout the day 

wind_power = [1] * cfg.K
wind_power_frac = list()
for elements in wind_power:
    wind_power_frac.append(elements/(cfg.K))


#%%Now adding together to get total energy distribution: 

#Addtion of solar & wind distributions 
total_distribution_sust = list()
for i in range(cfg.K):
    total_distribution_sust.append(w_solar*solar_power_frac[i]
                                   + w_wind*wind_power_frac[i]
                                   )

#finding distribution of amount of MWh's sustainable energy during the day
E_total_sust = list()
for i in range(cfg.K):
    E_total_sust.append(E_daily_sust*total_distribution_sust[i])

total_energy_ones = [1] * cfg.K
E_total_unsust = list()
for elements in range(cfg.K):
    E_total_unsust.append(total_energy_ones[i]*E_daily_unsust/cfg.K)

#Value 
print(E_total_sust, ' - In MWh per timeslot (k)')
print(E_total_unsust, ' - In MWh per timeslot (k) ')  
print(365.0*(sum(E_total_sust) + sum(E_total_unsust)), 'MWh')  #Verification

#End note: These two lists above can be used in simple.py, 
#          SimpleNet = grid.net, part.
#          and should make our estimation of daily power distributions due to 
#          solar/wind more accurate            


#%%Done 