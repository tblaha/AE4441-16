#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:17:38 2020

@author: tblaha
"""

import numpy as np

#%% manual configuration

# rng config
seed = 2

# car config
N = 50  # number of cars

# grid config
grid_setting = -1

# consumer config kW
cons_mean = 30000
cons_peak = 38000

if grid_setting == 1:
    rel_car_distribution = [1]
    rel_cons_distribution = [1]
elif grid_setting == 3:
    rel_car_distribution = [2, 2, 1]
    rel_cons_distribution = [3, 1, 1]
elif grid_setting == -1:
    rel_car_distribution = [2, 1.5, 0.2, 0, 0.7, 1.6, 3.6, 0.2,
                             0.25, 0.7, 6, 3, 3, 0, 1, 1]
    rel_cons_distribution = [2, 1.5, 0.2, 0, 0.7, 1.6, 3.6, 0.2,
                             0.25, 0.7, 6, 3, 3, 0, 1, 1]
    

# powerplant config
max_caps = {"Biomass": 15000,
            "Wind": 20000,
            "Solar": 5000,
            "Cable": 25000,
            }

# power cost
cs = 1  # relative cost of sustainable power
cu = 2  # relative cost of unsustainable power

# day config
K = 24  # number of timeslots --> minimum 3
dtday = 10  # daylight hours

# charger config
num_work_charger = np.ceil(0.5*N)
p_work_charger_type = np.array([0.05, 0.25, 0.25, 0.45])
p_home_charger_type = np.array([0, 0, 0.3, 0.7])


#%% helper calculations 

# hours per timeslot
dt = 24/K * np.ones(K) 

# mean daytime array for timeslots range(K)
t = np.zeros(K)
t[1:] = np.cumsum(dt)[0:-1]
t = t + dt/2

