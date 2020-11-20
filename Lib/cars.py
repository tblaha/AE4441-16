import pandas as pd
import numpy as np
from numpy import random as npr
from Lib.constants import MTK, RE
from Lib.grid import grid
from Lib import SimConfig as cfg

npr.seed(cfg.seed)


def rel_assign(w, N):
    # w: relative weights categories (list or np array)
    # N: target number of items assigned
    # a: assignment as integer numpy array
    rw = w / np.sum(w)

    lamb = 1
    while True:
        # basic concept: try scaling the cro by an integer and check resulting 
        # distribution of cars. Keep raising the integer lamb and once we 
        # overshoot the cfg.N target --> decrement lamb again and randomly add 
        # the missing ones from 1 up to len(cro) types
        # 
        # I haven't checked the math, but I believe that the amount of cars to be
        # added is always less or equal len(cro) and thus the code below should 
        # never fail.
        
        Nc = np.sum(np.floor(lamb * rw)).astype(int)
        if Nc <= N:
            lamb += 1
        else:
            lamb -= 1
            a = np.floor(lamb * rw).astype(int)
            pN = np.sum(a)
            
            if (N - pN) > len(rw):
                raise("Amount of items to be randomly added too large")
                    
            if pN < N:
                # scaling cro didn't fully work, we have to randomly add a few cars
                r = np.arange(len(rw))
                npr.shuffle(r)
                
                a[r[:(N - pN)]] += 1
            elif pN == N:
                pass # do nothing
            else:
                raise("something went wrong with dynamic assignment wrong")
            return a


#%% car_stat frame
car_stat = pd.DataFrame(
    {'Car Type': ['Tesla Model 3','Tesla Model Y','Tesla Model X','Chevy Bolt',
                  'Tesla Model S','NISSAN LEAF','Audi e-tron','BMW i3'
                  ]}
    )
car_stat['Battery size'] = [50, 50, 100, 60, 100, 40, 95, 42.2]
car_stat['Range'] = MTK * np.array([240, 240, 250, 238, 285, 150, 204, 153])
car_stat['kWh/km'] = car_stat['Battery size']/car_stat['Range']

car_relative_ownership = np.array([4, 2, 2, 1, 1, 8, 4, 4])

car_stat['Amount owned'] = rel_assign(car_relative_ownership, cfg.N)

assert(sum(car_stat['Amount owned']) == cfg.N)



#%% car_data frame --> timeslot-independent attributes

entities = np.arange(0, sum(car_stat['Amount owned']))
current_entity = 0

cars_data = pd.DataFrame({'CarId': entities, 
                          'Car Type': entities, 
                          'Distance Driven': entities,
                          'kWh/km': entities, 
                          'Battery size': entities,
                          'time': entities,
                          'GridConn': entities,
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
                              'GridConn': str,
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

cars_data["Color"] = "Blue"
cars_data["Size"] = 30



#%% car_data frame --> time dependent attributes

# how many grid nodes?
G = len(grid)

# Repeat entries such that we have one per time slot per car
cars_data = cars_data.loc[
    cars_data.index.repeat(cfg.K)
    ].reset_index(drop=True)

# assign the cars to the grid nodes
rel_car_distribution  = [2, 2, 1]  # Ronne, Nexo, Tejn. hard coded for now 
car_distr = rel_assign(rel_car_distribution, cfg.N)
assert(sum(car_stat['Amount owned']) == cfg.N)

# stupid hack to get the array describing how many go to which city in another
# format so that it can be used for indexing. For instance:
# car_distr == [4 4 3]  --> car_alloc = [0 0 0 0 1 1 1 1 2 2 2]
car_alloc = [k for k in range(G) for l in range(car_distr[k])]

# randomize which cars will be assigned
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
    cars_data.loc[car_bool, "GridConn"] = grid_idxes
    
    
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
    

