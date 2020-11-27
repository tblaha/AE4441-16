#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:03:16 2020

@author: tblaha
"""

import numpy as np
import numpy.random as npr
import pandas as pd
import copy
import os


# import the global config
from Lib import SimConfig as cfg
npr.seed(cfg.seed)


#%% powerplant data frame --> timeslot-independent attributes

pp_data_base = pd.DataFrame(columns=["PPId",
                                     "Name",
                                     "Long", 
                                     "Lat",
                                     "Type",
                                     "Sustainability",
                                     "GridConn",
                                     "Color",
                                     "Size",
                                     ])



if cfg.grid_setting == 1:
    pp_data_base.loc["Kraftvaerk"] = [0, "Kraftvaerk",    14.6963, 55.0938, "Biomass", 
                                      "sustainable", "Ronne", "Brown", 80]
    pp_data_base.loc["WindWest"]   = [1, "WindWest",   14.7491, 55.0809, "Wind",
                                      "sustainable", "Ronne", "White", 80]
    pp_data_base.loc["Cable"]      = [2, "Cable",      14.6898, 55.1884, "Cable",
                                      "unsustainable", "Ronne", "Black", 80]
    pp_data_base.loc["SolarWest"]  = [3, "SolarWest",  14.7241, 55.1312, "Solar",
                                      "sustainable", "Ronne", "Orange", 80]
elif cfg.grid_setting == 3:
    pp_data_base.loc["Kraftvaerk"] = \
      [0, "Kraftvaerk", 14.6963, 55.0938, "Biomass", "sustainable", "Ronne", "Brown", 80]
    pp_data_base.loc["WindWest"]   = [1, "WindWest",   14.7491, 55.0809, "Wind",
                                      "sustainable", "Ronne", "White", 80]
    pp_data_base.loc["WindNorth"]  = [2, "WindNorth",  14.7564, 55.2552, "Wind",
                                      "sustainable", "Tejn",  "White", 80]
    
    pp_data_base.loc["WindEast"]   = [3, "WindEast",   15.0928, 55.0815, "Wind",
                                      "sustainable", "Nexo",  "White", 80]
    pp_data_base.loc["SolarWest"]  = [4, "SolarWest",  14.7241, 55.1312, "Solar",
                                      "sustainable", "Ronne", "Orange", 80]
    
    
    pp_data_base.loc["SolarNorth"] = [5, "SolarNorth", 14.8539, 55.2314, "Solar",
                                      "sustainable", "Tejn",  "Orange", 80]
    
    pp_data_base.loc["SolarEast"]  = [6, "SolarEast",  15.0877, 55.0408, "Solar",
                                      "sustainable", "Nexo",  "Orange", 80]
    pp_data_base.loc["Cable"]      = [7, "Cable",      14.6898, 55.1884, "Cable",
                                      "unsustainable", "Ronne", "Black", 80]
elif cfg.grid_setting == -1:
    pp_data_base.loc["Kraftvaerk", ["Long","Lat","Type","Sustainability","GridConn","Color","Size"]] = \
      [14.6963, 55.0938, "Biomass", "sustainable", "Ronne", "Brown", 80]
    
    pp_data_base.loc["WindNorth", ["Long","Lat","Type","Sustainability","GridConn","Color","Size"]] = \
      [14.740725, 55.237306, "Wind",    "sustainable", "Olsker", "White", 80]
    pp_data_base.loc["WindWest", ["Long","Lat","Type","Sustainability","GridConn","Color","Size"]] = \
      [14.74993, 55.18200, "Wind",    "sustainable", "Hasle", "White", 80]
    pp_data_base.loc["WindSouth", ["Long","Lat","Type","Sustainability","GridConn","Color","Size"]] = \
      [14.84812, 55.05616, "Wind",    "sustainable", "Akirkeby", "White", 80]
    pp_data_base.loc["WindEast", ["Long","Lat","Type","Sustainability","GridConn","Color","Size"]] = \
      [15.02331, 55.05478, "Wind",    "sustainable", "Bodilsker", "White", 80]

    pp_data_base.loc["SolarNorth", ["Long","Lat","Type","Sustainability","GridConn","Color","Size"]] = \
      [14.84209, 55.24465, "Solar",    "sustainable", "Olsker", "Orange", 80]
    pp_data_base.loc["SolarWest", ["Long","Lat","Type","Sustainability","GridConn","Color","Size"]] = \
      [14.73486, 55.11800, "Solar",    "sustainable", "RonneNord", "Orange", 80]
    pp_data_base.loc["SolarEast", ["Long","Lat","Type","Sustainability","GridConn","Color","Size"]] = \
      [15.09376, 55.01898, "Solar",    "sustainable", "Poulsker", "Orange", 80]
      
    pp_data_base.loc["SeaCable", ["Long","Lat","Type","Sustainability","GridConn","Color","Size"]] = \
      [14.669080, 55.167127, "Cable",    "unsustainable", "Hasle", "Black", 80]
    
    pp_data_base["PPId"] = range(9)
    pp_data_base["Name"] = pp_data_base.index
    
pp_data_base = pp_data_base.astype({"PPId": int,
                                    "Name": str,
                                    "Long": float, 
                                    "Lat": float,
                                    "Type": str,
                                    "Sustainability": str,
                                    "GridConn": str,
                                    "Color": str,
                                    "Size": float, 
                                    })



#%% get hourly availability for solar power

cwd = os.getcwd()       

#This excel file is for the 31st of March at latitude 55 (Bornholm)
#From site https://www.pveducation.org/pvcdrom/properties-of-sunlight/calculation-of-solar-insolation
#Concerns the average solar irradiation at that lattitude [kW/m2]
instance_name = './Lib/Solar_rad.xlsx' #Importing excel file with solar irradiance 

#Excel -> pandas dataframe -> numpy array 
df = pd.read_excel(os.path.join(cwd,instance_name)) 
array = df.values 
solardata = np.array(array)


# Creating a list of values (solar_irr_frac) that contains distribution of 
# solar irradiation throughout day 
#Beetje gebeund, but looks at solardata and takes middle point of each timeslot
#k as reference for the relative amount of solar energy received at that moment 

solar_power = list()
a = len(solardata)/cfg.K
b = 0.5*a
entries = list()
entries.append(b)
for k in range(cfg.K):
    c = b + k*a
    entries.append(c)

for k in range(len(solardata)):
      if k in entries: 
        solar_power.append((solardata[k][1]))

#Fraction of solar daily solar energy per timeslot (k)
solar_power_frac = solar_power/(sum(solar_power)) 


#%% get hourly availability of wind power

# https://www.researchgate.net/figure/Shares-of-PV-and-Wind-supply-hourly-pro-fi-le-2011_fig3_283240342

# fourier series

# fundamental
f0 = 1/24  # 1/h

# average 1, no low freq contributions
an = [1, 0, 0, 0, 0]
bn = [0, 0, 0, 0, 0]

# randomize magnitude and phase of the highest requencies
an[3:], bn[3:] = 0.5*(npr.random([2, 2])-0.5)

# synthesize using vectorized calculations
N = len(an)
argu = np.array(
    2*np.pi*f0 
    * np.matrix(cfg.t).T * np.arange(0, N)
    )

wind_power_frac = np.cos(argu) @ an - np.sin(argu) @ bn

# normalize to make sure that sum will be 1
wind_power_frac /= sum(wind_power_frac)


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
# cosine adjustment to guarantee daylight hours
lambda_sol = np.cos(2*np.pi/24 * (12 - cfg.dtday/2 ))  
cap_distr = {"Biomass": np.ones(cfg.K),
             # "Wind": 1 + 0.25 * np.sin(2*np.pi/24 * cfg.t),
             "Wind": wind_power_frac,
             # "Solar": np.maximum(0, lambda_sol - np.cos(2*np.pi/24 * cfg.t)),
             "Solar": solar_power_frac,
             "Cable": np.ones(cfg.K),
             }

for key, val in cfg.max_caps.items():
    pp_bool = pp_data["Type"] == key
    
    pp_data.loc[pp_bool, "Time"] = np.tile(np.arange(cfg.K), pp_num[key])
    pp_data.loc[pp_bool, "Cap"] = (
        cfg.max_caps[key] # max capacity 
        * np.tile(cap_distr[key] / np.max(cap_distr[key]), #normalized rel cap
                  pp_num[key]) # repeated for how many plants we have
        / pp_num[key])  # since cfg.max_caps is the overall cap; devide by 
                        # number of plants for this type of energy

    pp_data.loc[pp_bool, "Load"] = 0.0

pp_data = pp_data.astype({"Time": int,
                          "Cap": float,
                          "Load": float,
                          })
