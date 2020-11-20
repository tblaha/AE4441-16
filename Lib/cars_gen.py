import pandas as pd
import numpy as np
from numpy import random as npr
from Lib.constants import MTK, RE
from Lib.grid_gen import grid
from Lib import SimConfig as cfg

npr.seed(cfg.seed)

    
#%% helper functions

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


#%% car stats generation

#Random information
#https://support.fastned.nl/hc/en-gb/sections/115000180588-Vehicles-charging-tips
#https://www.myev.com/research/buyers-sellers-advice/comparing-all-2019-electric-vehicles
car_stat = pd.DataFrame(
    {'Car Type': ['Tesla Model 3','Tesla Model Y','Tesla Model X','Chevy Bolt',
                  'Tesla Model S','NISSAN LEAF','Audi e-tron','BMW i3'
                  ]}
    )
car_stat['Battery size'] = [50,50,100,60,100,40,95,42.2]
car_stat['Range'] = MTK * np.array([240, 240, 250, 238, 285, 150, 204, 153])
car_stat['kWh/km'] = car_stat['Battery size']/car_stat['Range']
car_relative_ownership = np.array([8000,4000,2000,2000,1000,1000,1000,740])

# generate actual distribution of cars based on the unified cfg.N parameter
car_stat['Amount owned'] = rel_assign(car_relative_ownership, cfg.N)
assert(sum(car_stat['Amount owned']) == cfg.N)  # make sure that it succeeded

# charger info
car_stat['175 kW Charger'] = [140,140,140,120,140,0,120,0]
car_stat['50 kW Charger'] = 8*[50]
car_stat['Standard 3-phase'] = 8*[22]
car_stat['Standard 1-phase'] = 8*[7]
car_stat['Homecharging'] = 8*[3.6]

# driving data -- distance
bornholm_data = [19740,33.8,0.613,0.03]
driven_distance_data = pd.DataFrame({'Average distance driven [km/day]': np.arange(0,150,5)})
driven_distance_data['Share of the cars [%]'] = [4,7,12,11,11,9,10,6,5,3,4,2,3,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0]
for i in range(0,driven_distance_data['Average distance driven [km/day]'].size):
    driven_distance_data.at[i, 'Number of cars'] = int(driven_distance_data['Share of the cars [%]'][i]/100*bornholm_data[0])

# driving data -- time
driven_time_data = pd.DataFrame({'Time of day [h]': np.arange(0,24)})
driven_time_data['Share driven cars [%]'] = [0,0,0,0,0,1,3,5,3,3,4,4,4,4,4,6,7,5,3,2,1,2,1,0]



#%% car_data frame --> timeslot-independent attributes

entities = np.arange(sum(car_stat['Amount owned']))
current_entity = 0
count2 = 30


cars_data_base = pd.DataFrame({'CarId': entities, 
                               'Car Type': entities, 
                               'Distance Driven': entities,
                               'kWh/km': entities, 
                               'Battery size': entities,
                               'Charger type': entities,
                               'Color': entities,
                               'Size': entities,
                               })
cars_data_base = cars_data_base.astype({'CarId': int, 
                                        'Car Type': str, 
                                        'Distance Driven': float,
                                        'kWh/km': float,
                                        'Battery size': float,
                                        'Charger type': int,
                                        'Color': str,
                                        'Size': float,
                                        })

for i in range(0,car_stat['Car Type'].size):
    # car type
    cars_data_base.loc[ 
        current_entity:int(current_entity + car_stat['Amount owned'][i]),
        'Car Type'
        ] = car_stat['Car Type'][i]
    
    # battery size
    cars_data_base.loc[
        current_entity:int(current_entity + car_stat['Amount owned'][i]),
        'Battery size'
        ] = car_stat['Battery size'][i]
    
    current_entity = int(current_entity + car_stat['Amount owned'][i]) 

# car distance and efficiency
beun_time = [0,1/3,11/3,11/3,4,6,2,1]
for i in range(0,sum(car_stat['Amount owned'])):
    count = npr.randint(0,29)
    while count != count2:
        if driven_distance_data.at[count, 'Number of cars'] > 0:     
            cars_data_base.at[i, 'Distance Driven'] = driven_distance_data.at[count, 'Average distance driven [km/day]']
            driven_distance_data.at[count, 'Number of cars'] = driven_distance_data.at[count, 'Number of cars'] - 1
            count2 = count
        else: 
            count = npr.randint(0,29)
            count2 = 30
            
    # cars_data.at[i, 'kWh/km'] = random.randint(9,14)  # sounds way too high!
    cars_data_base.at[i, 'kWh/km'] = npr.randint(9,14) * 2/100
    
    # somehow always gives 1
    # cars_data.at[i, 'Grid connection 1'] = int(2 - npr.random() - beun_time[0]/100)
    # cars_data.at[i, 'Grid connection 2'] = int(2 - npr.random() - beun_time[1]/100)
    # cars_data.at[i, 'Grid connection 3'] = int(2 - npr.random() - beun_time[2]/100)
    # cars_data.at[i, 'Grid connection 4'] = int(2 - npr.random() - beun_time[3]/100)
    # cars_data.at[i, 'Grid connection 5'] = int(2 - npr.random() - beun_time[4]/100)
    # cars_data.at[i, 'Grid connection 6'] = int(2 - npr.random() - beun_time[5]/100)
    # cars_data.at[i, 'Grid connection 7'] = int(2 - npr.random() - beun_time[6]/100)
    # cars_data.at[i, 'Grid connection 8'] = int(2 - npr.random() - beun_time[7]/100)
    cars_data_base.at[i, 'Charger type'] = 1 #random.randint(0,1)
    

# plotting attributes (same for all cars)
cars_data_base["Color"] = "Blue"
cars_data_base["Size"] = 30.



#%% car_data frame --> time dependent attributes

# how many grid nodes?
G = len(grid)

# Repeat entries such that we have one per time slot per car
cars_data = cars_data_base.loc[
    cars_data_base.index.repeat(cfg.K)
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
    cars_data.loc[car_bool, ["Time"]] = np.arange(cfg.K).astype(int)
    
    
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
    cars_data.loc[car_bool, ["Load"]] = 0.
    
    
cars_data = cars_data.astype({'Time': int,
                              'GridConn': str,
                              'Long': float,
                              'Lat': float,
                              'Charger type': int,
                              'Load': float,
                              })

    