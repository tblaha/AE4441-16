#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:41:26 2020

@author: tblaha
"""

import numpy as np
import pandas as pd
from gurobipy import GRB
import copy

# import the global config
from Lib import SimConfig as cfg


#%% grid data frame

# generate grid connection and location
grid = pd.DataFrame(columns=["Long", "Lat", "2SigRadius", "Type", "Color", "Size"])
grid = grid.astype({"Long": float, 
                    "Lat": float, 
                    "2SigRadius": float,
                    "Type": str, 
                    "Color": str, 
                    "Size": float,
                    })
grid.loc["Ronne"] = [14.7110, 55.0966, 3000, "60kV Station", "Orange", 50]
grid.loc["Nexo"]  = [15.1291, 55.0585, 3000, "60kV Station", "Orange", 50]
grid.loc["Tejn"]  = [14.8360, 55.2474, 3000, "60kV Station", "Orange", 50]



#%% powerplant data frame --> timeslot-independent attributes

pp_data = pd.DataFrame(columns=["Long", 
                                "Lat",
                                "Type",
                                "Sustainability",
                                "GridConn",
                                "Color",
                                "Size",
                                "time",
                                "Cap",
                                "Load",
                                ])

pp_data = pp_data.astype({"Long": float, 
                          "Lat": float,
                          "Type": str,
                          "Sustainability": str,
                          "GridConn": str,
                          "Color": str,
                          "Size": float, 
                          "time": int,
                          "Cap": float,
                          "Load": float,
                          })

pp_data.loc["Biomass"]    = [14.6963, 55.0938, "Biomass", "sustainable",   "Ronne", "Green", 30, 0, 0, 0]
pp_data.loc["WindWest"]   = [14.7491, 55.0809, "Wind",    "sustainable",   "Ronne", "Green", 30, 0, 0, 0]
pp_data.loc["WindNorth"]  = [14.7564, 55.2552, "Wind",    "sustainable",   "Tejn",  "Green", 30, 0, 0, 0]
pp_data.loc["WindEast"]   = [15.0928, 55.0815, "Wind",    "sustainable",   "Nexo",  "Green", 30, 0, 0, 0]
pp_data.loc["SolarWest"]  = [14.7241, 55.1312, "Solar",   "sustainable",   "Ronne", "Green", 30, 0, 0, 0]
pp_data.loc["SolarNorth"] = [14.8539, 55.2314, "Solar",   "sustainable",   "Tejn",  "Green", 30, 0, 0, 0]
pp_data.loc["SolarEast"]  = [15.0877, 55.0408, "Solar",   "sustainable",   "Nexo",  "Green", 30, 0, 0, 0]
pp_data.loc["Cable"]      = [14.6898, 55.1884, "Cable",   "unsustainable", "Ronne", "Red",   30, 0, 0, 0]



#%% powerplant data frame --> timeslot-dependent attributes

# figure out how many pwoer plants we have per type (wind, solar...)
pp_num = copy.deepcopy(cfg.max_caps)
for key, val in cfg.max_caps.items():
    pp_num[key] = sum(pp_data["Type"] == key)
    
# Repeat entries such that we have one per time slot per powerplant
pp_data = pp_data.loc[
    pp_data.index.repeat(cfg.K)
    ].reset_index(drop=True)


# capacity time distribution
lambda_sol = np.cos(2*np.pi/24 * (12 - cfg.dtday/2 ))  # cosine adjustment to guarantee daylight hours
cap_distr = {"Biomass": np.ones(cfg.K),
             "Wind": 1 + 0.25 * np.sin(2*np.pi/24 * cfg.t),
             "Solar": np.maximum(0, lambda_sol - np.cos(2*np.pi/24 * cfg.t)),
             "Cable": np.ones(cfg.K),
             }

for key, val in cfg.max_caps.items():
    pp_bool = pp_data["Type"] == key
    
    pp_data.loc[pp_bool, "time"] = np.tile(np.arange(cfg.K), pp_num[key])
    pp_data.loc[pp_bool, "Cap"] = (
        cfg.max_caps[key] # max capacity 
        * np.tile(cap_distr[key] / np.max(cap_distr[key]), # normalized rel cap
                  pp_num[key]) # repeated for how many plants we have
        / pp_num[key])  # since cfg.max_caps is the overall cap; devide by 
                        # number of plants for this type of energy



#%% consumer data frame --> time independent data

cons_data = pd.DataFrame(columns=["Long",
                                  "Lat",
                                  "GridConn",
                                  "Color",
                                  "RelCons",
                                  "Size",
                                  "Peak",
                                  "time",
                                  "Load",
                                  ])
cons_data = cons_data.astype({"Long": float, 
                              "Lat": float,
                              "GridConn": str,
                              "Color": str,
                              "RelCons": float, 
                              "Size": float, 
                              "Peak": float,
                              "time": int,
                              "Load": float,
                              })

for index, row in grid.iterrows():
    gc_loc = row[["Long", "Lat"]].to_numpy()
    centre_vector = (np.array([14.9291, 55.1146]) - gc_loc)
    dem_loc = gc_loc + centre_vector / np.linalg.norm(centre_vector) * 0.025
    
    cons_data.loc[index, ["Long", "Lat"]] = dem_loc
    cons_data.loc[index, ["GridConn"]] = index
    cons_data.loc[index, ["Color", "RelCons", "Size", "Time", "Load"]] \
        = ["Purple", 1, 30, 0, 0]
    

# normalize Relative Consumption
cons_data["RelCons"] = cons_data["RelCons"] / cons_data["RelCons"].sum()
cons_data["Peak"] = cfg.cons_peak * cons_data["RelCons"]



#%% consumer data frame --> time dependent data

# implement quad-linear demand curve
# https://www.eia.gov/todayinenergy/detail.php?id=830
def tot_cons(t, avg, peak):
    ni = (24 * avg - 5/2 * peak) / 29.5 # night power
    if (t >= 0) & (t < 6):
        return ni
    elif (t >= 6) & (t < 9):
        return ni * (1 + 1/2 * (t - 6)/3)
    elif (t >= 9) & (t < 19):
        return ni * 3/2
    elif (t >= 19) & (t < 24):
        return peak - (peak - ni) * (t - 19)/5
    else:
        raise("t outside 0-24h interval")

tot_cons_dem = np.array([tot_cons(t, cfg.cons_mean, cfg.cons_peak) 
                         for t in cfg.t
                         ])

# Repeat entries such that we have one per time slot per powerplant
cons_data = cons_data.loc[
    cons_data.index.repeat(cfg.K)
    ].reset_index(drop=True)


for index, row in grid.iterrows():
    cons_bool = cons_data["GridConn"] == index
    local_cons = cons_data.loc[cons_bool, "RelCons"].iat[0]
    
    cons_data.loc[cons_bool, "time"] = np.arange(cfg.K)
    cons_data.loc[cons_bool, "Load"] = local_cons * tot_cons_dem



#%% Network class definition

class net:
    def __init__(self,
                 ps_s,  # available sustainable power supply for each time j
                 cs,    # cost of sustainable power for each time j
                 pu_s,  # available UNsustainable power supply for each time j
                 cu,    # cost of UNsustainable power for each time j
                 pd,    # invariant consumer demand for each time j
                 ):
        """ ps_s, cs, pu_s, cu, pd  ---> list of length cfg.K (the amount of 
                                                               timeslots)
        """
        
        # save customer demand in internal memory
        self.pd = pd
        
        # instantiate power-plant objects (defined below) for the supplies
        self.sus_power = powerplant("sus", ps_s, cs)
        self.unsus_power = powerplant("unsus", pu_s, cu)
        
    
    def create_vars_obj(self, 
                        model,  # the gurobi model to which to add the vars
                        ):
        """ Add the variables for the powerplants supplies to model.
        Also, generate their coefficients in the objective function row.
        
        It's using the "create_vars_obj" method of the powerplant object, 
        defined below
        """
        
        # list of Sustainable power variables for each j
        self.PS = self.sus_power.create_vars_obj(model)
        
        # list of Unsustainable power variables for each j
        self.PU = self.unsus_power.create_vars_obj(model)
    
    
    def create_constrs(self, 
                       model,  # the gurobi model to which to add the constrs
                       cars,   # list of car objects
                       ):
        """ Add flow constraint to "model", for each different timeslot, based 
        on a single-node model of the grid (direct connection from/to all 
                                            supplies/demands)
            """
        for j in range(cfg.K):  # for each time slot j:
            model.addConstr(self.PS[j] + self.PU[j]   # supply energy
                == self.pd[j]  # customer demand
                + sum( # sum over all cars
                      cars[i].Xi[j] # battery charging power 
                                    # + dot product of mode binaries and loss 
                                    # list for the different modes
                      + np.array(cars[i].Yi[j]) @ cars[i].ch[j].P_loss 
                      for i in range(cfg.N)
                      ),
                name="C_node_" + str(j),
                )


#%% Powerplant class that is mentioned and instantiated above

class powerplant:
    
    def __init__(self, 
                 name,
                 p_s,  # supply capabilities
                 c,    # cost
                 ):
        """ implements the variable/objective/constraint generation for a 
        powerplant with :
            a name
            supply capabilities "p_s"
            supply cost "c"
            """
            
        # save inputs in internal memory
        self.name = name
        self.p_s = p_s
        self.c = c
        
        
    def create_vars_obj(self, model):
        """ Add the supply variables to "model", for each different timeslot
        (ps_j and pu_j) with their bounds and with their contribution to the 
        objective function.
            """
        
        P = list()
        for j in range(cfg.K):  # for each time slot j:
                
            # this does the heavy lifting of adding the vars to model
            p = model.addVar( 
                    lb = 0.0,
                    ub = self.p_s[j],  # upper bound: 
                    obj = self.c[j] * cfg.dt[j], # coefficient in objective function
                    vtype=GRB.CONTINUOUS,
                    name="P_" + self.name + "_" + str(j)
                    )
                
            # this only saves the gurobi variable objects to a list for future 
            # reference in the node constraints
            P.append(p) 
            
        return P
            
            