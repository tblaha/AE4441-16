#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:33:12 2020

@author: tblaha
"""

import numpy as np
from gurobipy import GRB

from Lib import SimConfig as cfg

class car:
    """ Electriv vehicle class characterizing owner and charger
    """
    def __init__(self, 
                 name,      # string for identifying the car
                 s_day,     # km driven each day
                 E_eff,     # kWh electrical energy used per km
                 E_max,     # battery size in kWh
                 t_conn,    # list of timeslots connected to grid
                 ch_type,   # charger type
                 ):
        self.name    = name
        self.s_day = s_day  # km/day
        self.E_eff = E_eff  # kWh/km
        self.E_max = E_max  # kWh
        self.E_min = 0.1*E_max  # kWh
        self.E_state = 0.5*E_max  # charge at start of day
        self.t_conn = np.array(t_conn).astype(bool)  # bool
        self.ch = charger(ch_type)
        
    def create_vars(self, model):
        self.Xs = list()
        self.Ys = list()
        R = list()
        
        for j in range(cfg.K):
            # charging power variable
            x = model.addVar(
                lb = min(self.ch.P),
                ub = max(self.ch.P),
                vtype=GRB.CONTINUOUS,
                name="X_" + self.name + "_" + str(j)
                )
            self.Xs.append(x)
            
            # charging mode binaries
            Ym = list()
            for m in range(self.ch.M):
                y = model.addVar(
                    vtype=GRB.BINARY,
                    name="Y_" + self.name + "_" + str(j) + "_" + str(m)
                    )
                Ym.append(y)
            self.Ys.append(Ym)
            
        return self.Xs, self.Ys
    
    def create_constrs(self, model):
        self.Cs_OOOM = list()
        self.Cs_Power = list()
        self.Cs_E_lb = list()
        self.Cs_E_ub = list()
        self.Cs_E_net = list()
        
        for j in range(cfg.K):
            OOOM = model.addConstr(
                sum(self.Ys[j]) == 1,
                name="C_" + self.name + "_" + str(j) + "_OOOM"
                )
            Power = model.addConstr(
                self.Xs[j] == sum(
                    self.Ys[j][m] * self.ch.P[m] for m in range(self.ch.M)
                    ),
                name="C_" + self.name + "_" + str(j) + "_" + "P"
                )
            self.Cs_OOOM.append(OOOM)
            self.Cs_Power.append(Power)
            
            
            if j < cfg.K - 1:
                E_lb = model.addConstr( 
                   self.E_state + sum(self.Xs[jj] * cfg.dt[jj] for jj in range(j+1))
                       >= self.E_min,
                   name="C_" + self.name + "_" + str(j) + "_" + "E_lb"
                   )
                E_ub = model.addConstr( 
                   self.E_state + sum(self.Xs[jj] * cfg.dt[jj] for jj in range(j+1))
                       <= self.E_max,
                   name="C_" + self.name + "_" + str(j) + "_" + "E_ub"
                   )
                self.Cs_E_lb.append(E_lb)
                self.Cs_E_ub.append(E_ub)

            
        self.E_net = model.addConstr( 
           sum(self.Xs[j] * cfg.dt[j] for j in range(cfg.K))
               >= self.E_eff * self.s_day,
           name="C_" + self.name + "_" + "E_net"
           )
            
        return self.Cs_OOOM, self.Cs_Power, self.Cs_E_lb, self.Cs_E_ub, self.E_net
        
        
class charger:
    def __init__(self, ch_type):
        if ch_type == 1:
            self.M = 6  # charging modes
            self.P = np.array([-11, -5, -2, 2, 5, 11])  # kW power
            self.P_loss = np.abs(self.P  # power lost ontop of self.P
                                 * np.array([0.1, 0.12, 0.15, 0.1, 0.07, 0.06])
                                 )
        else:
            raise NotImplementedError("Only Charger Type 1 implemented.")
        