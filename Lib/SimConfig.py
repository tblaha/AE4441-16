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
N = 50  # number of cars

# powerplant config
max_caps = {"Biomass": 15000,
            "Wind": 25000,
            "Solar": 10000,
            "Cable": 30000,
            }

# consumer config kW
cons_mean = 30000
cons_peak = 40000

# day config
K = 12  # number of timeslots
dtday = 10  # daylight hours


#%% helper calculations 

# hours per timeslot
dt = 24/K * np.ones(K) 

# mean daytime array for timeslots range(K)
t = np.zeros(K)
t[1:] = np.cumsum(dt)[0:-1]
t = t + dt/2

