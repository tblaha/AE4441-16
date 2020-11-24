#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:17:38 2020

@author: tblaha
"""

import numpy as np


#%% manual configuration

# rng config
seed = 1

# car config
N = 100  # number of cars

# powerplant config
max_caps = {"Biomass": 15000,
            "Wind": 25000,
            "Solar": 10000,
            "Cable": 80000,
            }

# power cost
cs = 1  # relative cost of sustainable power
cu = 2  # relative cost of unsustainable power

# consumer config kW
cons_mean = 30000
cons_peak = 35000

# day config
K = 12  # number of timeslots
dtday = 10  # daylight hours

# charger config
num_work_charger = np.ceil(0.1*N)
p_work_charger_type = np.array([0.05, 0.25, 0.25, 0.45])
p_home_charger_type = np.array([0, 0, 0.3, 0.7])


#%% helper calculations 

# hours per timeslot
dt = 24/K * np.ones(K) 

# mean daytime array for timeslots range(K)
t = np.zeros(K)
t[1:] = np.cumsum(dt)[0:-1]
t = t + dt/2

