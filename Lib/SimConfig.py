#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:17:38 2020

@author: tblaha
"""

import numpy as np

N = 2  # number of cars
K = 3  # number of timeslots
dt = 24/K * np.array([1, 1, 1])  # hours per timeslot