#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:41:26 2020

@author: tblaha
"""

import numpy as np
from gurobipy import GRB

from Lib import SimConfig as cfg

class net:
    def __init__(self,
                 ps_s,
                 cs,
                 pu_s,
                 cu,
                 pd,    # invariant consumer demand
                 ):
        self.pd = pd
        self.sus_power = powerplant("sus", ps_s, cs)
        self.unsus_power = powerplant("unsus", pu_s, cu)
    
    def create_vars_obj(self, model):
        self.PS = self.sus_power.create_vars_obj(model)
        self.PU = self.unsus_power.create_vars_obj(model)
        
        return self.PS, self.PU
        
    def create_constrs(self, model, X_cars):
        C_node = list()
        for j in range(cfg.K):
            cj = model.addConstr(self.PS[j] + self.PU[j]
                              == self.pd[j] + sum(X_cars[i][j] for i in range(cfg.N)),
                              name="C_node_" + str(j),                      
                              )
            C_node.append(cj)
        return C_node
    
class powerplant:
    def __init__(self, 
                 name,
                 p_s,  # supply capabilities
                 c,    # relative cost
                 ):
        self.name = name
        self.p_s = p_s
        self.c = c
        
    def create_vars_obj(self, model):
        Ps = list()
        for j in range(cfg.K):
            p = model.addVar(
                lb = 0.0,
                ub = self.p_s[j],
                obj = self.c[j] * cfg.dt[j],  # coefficient in objective function
                vtype=GRB.CONTINUOUS,
                name="P_" + self.name + "_" + str(j)
                )
            Ps.append(p)
            
        return Ps