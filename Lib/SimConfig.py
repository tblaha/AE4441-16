#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:17:38 2020

@author: tblaha
"""

import numpy as np

N = 15  # number of cars
K = 8  # number of timeslots
dt = 24/K * np.ones(8) # hours per timeslot