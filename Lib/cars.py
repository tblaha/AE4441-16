import pandas as pd
import numpy as np
from numpy import random as npr
from Lib.constants import MTK, RE
from Lib.grid import grid
from Lib import SimConfig as cfg

npr.seed(cfg.seed)



#%% car_stat frame
car_stat = pd.DataFrame(
    {'Car Type': ['Tesla Model 3','Tesla Model Y','Tesla Model X','Chevy Bolt',
                  'Tesla Model S','NISSAN LEAF','Audi e-tron','BMW i3'
                  ]}
    )
car_stat['Battery size'] = [50, 50, 100, 60, 100, 40, 95, 42.2]
car_stat['Range'] = MTK * np.array([240, 240, 250, 238, 285, 150, 204, 153])
car_stat['kWh/km'] = car_stat['Battery size']/car_stat['Range']

car_stat['Amount owned'] = [2, 1, 1, 0, 0, 0, 0, 1]



#%% car_data frame --> timeslot-independent attributes

entities = np.arange(0, sum(car_stat['Amount owned']))
current_entity = 0

cars_data = pd.DataFrame({'CarId': entities, 
                          'Car Type': entities, 
                          'Distance Driven': entities,
                          'kWh/km': entities, 
                          'Battery size': entities,
                          'time': entities,
                          'GridNode': entities,
                          'Long': entities,
                          'Lat': entities,
                          'Charger type': entities,
                          })
cars_data = cars_data.astype({'CarId': int, 
                              'Car Type': str, 
                              'Distance Driven': float,
                              'kWh/km': float,
                              'Battery size': float,
                              'time': int,
                              'GridNode': str,
                              'Long': float,
                              'Lat': float,
                              'Charger type': int,
                              })

# car type
for i in range(0,car_stat['Car Type'].size):
    # car type
    cars_data.loc[ 
        current_entity:int(current_entity + car_stat['Amount owned'][i]),
        'Car Type'
        ] = car_stat['Car Type'][i]
    
    # battery size
    cars_data.loc[
        current_entity:int(current_entity + car_stat['Amount owned'][i]),
        'Battery size'
        ] = car_stat['Battery size'][i]
    
    current_entity = int(current_entity + car_stat['Amount owned'][i]) 

# car distance and efficiency
for i in range(0,sum(car_stat['Amount owned'])):
    # randomize efficiency and distance driven
    cars_data.at[i, 'Distance Driven'] = npr.randint(1,6)*10
    # cars_data.at[i, 'kWh/km'] = npr.randint(9,14) # sounds way too high!
    cars_data.at[i, 'kWh/km'] = npr.randint(9,14) * 2/100



#%% car_data frame --> time dependent attributes

# how many grid nodes?
G = len(grid)

# Repeat entries such that we have one per time slot per car
cars_data = cars_data.loc[
    cars_data.index.repeat(cfg.K)
    ].reset_index(drop=True)

car_dist  = [2, 2, 1]  # make this dynamic
car_alloc = [k for k in range(G) for l in range(car_dist[k])]
npr.shuffle(car_alloc)

# for each car, do:
for i, c in enumerate(car_alloc):
    # figure out which lines in the cars_data frame belong to car i
    car_bool = cars_data["CarId"] == i
    
    # add timeslot integers
    cars_data.loc[car_bool, ["time"]] = np.arange(cfg.K).astype(int)
    
    
    ######## add grid connection names to cars_data
    # figure out what the grid nodes are called that have been assigned in the 
    # car_alloc array that has been randomized by npr.shuffle
    grid_idxes = grid.index[c]
    
    # add those grid node names to the cars_data frame
    cars_data.loc[car_bool, "GridNode"] = grid_idxes
    
    
    ######### randomize coordinate locations
    # we need:
    rad = grid.loc[grid_idxes, "2SigRadius"]           # 95.7% radius in m
    long, lat = grid.loc[grid_idxes, ["Long", "Lat"]]  # coordinates
    
    # bi-variate normal distribution with mean and covariance matrix
    mu = np.array([long, lat])
    # convert 2 sigma radius in m to degrees long and lat
    sx, sy = (rad/2  # convert 2 sigma to 1 sigma
        / (RE * np.pi/180  # one arc-degree on Earth's surface
           * np.array([np.cos(lat*np.pi/180),  # correct for parallels getting 
                                               # shorter near poles
                       1])
              ))
    # covariance matrix with 0 correlation
    cov = np.diag(np.array([sx, sy])**2)
    
    # draw from multivariate normal
    cars_data.loc[car_bool, ["Long", "Lat"]]\
        = npr.multivariate_normal(mu, cov, size=1)[0]
    
    
    ######## charger connections during the timeslots
    cars_data.loc[car_bool, ["Charger type"]] = 1  # for now
    
    # temperary data for testing visualization
    cars_data.loc[car_bool, ["Cap"]] = 11
    cars_data.loc[car_bool, ["Load"]] = [5, -7, 11]

