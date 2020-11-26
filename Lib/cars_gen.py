import pandas as pd
import numpy as np
from scipy.integrate import quad
from numpy import random as npr
from Lib.constants import RE
from Lib.grid_gen import grid
from Lib import SimConfig as cfg

npr.seed(cfg.seed)

    
#%% helper functions

def relative_assign(w, N):
    # w: relative weights categories (list or np array)
    # N: target number of items assigned
    
    # initial guess
    rw = np.round(w / np.sum(w) * N)
    
    # discrepancy
    Delta = N - np.sum(rw)
    
    # decrease most common item
    rw[np.argmax(rw)] += Delta
    
    return rw.astype(int)


def change_hist_bins(w, B):
    
    # original number of bins and indices
    N = len(w)
    orig_idxs = np.arange(0, N)
    
    # new indices 
    idxs = np.linspace(0, N-1, B+1)

    rw = np.zeros(B)
    for j in range(B):
        # integrate an interpolation of the array w from over the new bins 
        # idxs[j] to idxs[j-1]
        rw[j], __ = quad(lambda x: np.interp(x, orig_idxs, w),
                            idxs[j], 
                            idxs[j+1],
                            )
    
    return rw


def draw_from_hist(bin_mids, hist, N):
    # bin_mids:  midpoints of the histogram bins (m dimensional array)
    # hist:      the amount of datapoints in each of the bins_mids
    # N:         scalar: how many points do you want generated?
    
    # set up CDF
    cdf = np.cumsum(hist)
    cdf = cdf / cdf[-1]
    
    # generate uniform scalars from 0 to 1
    U = npr.random(N)
    
    # figure out the indices of the bins that the U's landed in
    bin_idxs = np.searchsorted(cdf, U)
    
    vals = np.array(bin_mids)[bin_idxs]
    
    return vals



#%% car stats generation

#Random information
#https://support.fastned.nl/hc/en-gb/sections/115000180588-Vehicles-charging-tips
#https://www.myev.com/research/buyers-sellers-advice/comparing-all-2019-electric-vehicles
# Amounts are estimated and the rest is public data
car_stat = pd.DataFrame({'Car Type': ['Renault Zoe','Tesla Model 3',
                                      'VW e-Golf', 'Hyundai Kona',
                                      'Audi e-Tron']
                         })
car_stat['Percentage owned'] = [32,28,16,12,12]
car_stat['Battery size'] = [52,47.5,32,39.2,64.7]
car_stat['Range'] = [315,320,190,255,280]
car_stat['kWh/km'] = car_stat['Battery size']/car_stat['Range']

# faster and a bit cleaner that the previous for loop
car_stat['Amount owned'] = relative_assign(car_stat['Percentage owned'],
                                           cfg.N)



#%% chargers
# Averages are taken from the fastned website and IEC - 61851-1
charger_stat = pd.DataFrame(columns = car_stat["Car Type"].to_list())
charger_stat.loc['Mode 4 175 kW']  = [41,105,39,35,115]
charger_stat.loc['Mode 4 50 kW']   = [41,45,39,35,50]
charger_stat.loc['Mode 2 3-phase'] = [22,11,7.2,11,11]
charger_stat.loc['Mode 2 1-phase'] = [7.4,7.4,7.2,7.4,7.4]

# add id column
charger_stat["ChargerId"] = np.arange(4).astype(int)



#%% Driving distance/time

# Averages are read from graphs of Bornholm
bornholm_data = [19740,33.8,0.613,0.03]
driven_distance_data = pd.DataFrame(
    {'Average distance driven [km/day]': np.arange(0,150,5),
     'Share of the cars [%]': [4,7,12,11,11,9,10,6,5,3,4,2,3,1,
                               1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0]
     })

driven_distance_data["Number of cars"] \
    = (driven_distance_data['Share of the cars [%]']/100
       * bornholm_data[0]
       ).astype(int)
    
# Averages are read from graphs of Bornholm
driven_time_data = pd.DataFrame(
  {'Time of day [h]': np.arange(0,24),
   'Share driven cars [%]': [0,0,0,0,0,1,3,5,3,3,4,4,4,4,4,6,7,5,3,2,1,2,1,0],
   })



#%% car_data_base frame --> timeslot-independent attributes

entities = np.arange(0,sum(car_stat['Amount owned']))
current_entity = 0
count2 = 30


cars_data_base = pd.DataFrame({'CarId': entities, 
                               'Car Type': entities, 
                               'Distance Driven': entities,
                               'kWh/km': entities, 
                               'Battery size': entities,
                               'Color': entities,
                               'Size': entities,
                               })
cars_data_base = cars_data_base.astype({'CarId': int, 
                                        'Car Type': str, 
                                        'Distance Driven': float,
                                        'kWh/km': float,
                                        'Battery size': float,
                                        'Color': str,
                                        'Size': float,
                                        })


### basic car properties
n_repeats = car_stat['Amount owned']
repeat_cats = ["Car Type", "Battery size", "kWh/km"]
for cat in repeat_cats:
    cars_data_base[cat] = car_stat[cat].repeat(n_repeats).to_list()

# for plotting
cars_data_base["Color"] = "Blue"
cars_data_base["Size"]  = 30


#### assign driven distance
# for i in range(0,cars_data_base['Car Type'].size):
# # The distance driven by a car is randomly assigned from the 
# driven_distance_data. This does not work perfectly as whole percentages are 
# used in the original data
#     count = npr.randint(0,29)
#     while count != count2:
#         if driven_distance_data['Number of cars'][count] > 0:     
#             cars_data_base.at[i, 'Distance Driven'] \
#                 = driven_distance_data['Average distance driven [km/day]']\
#                                       [count]
#             driven_distance_data['Number of cars'][count]\
#                 = driven_distance_data['Number of cars'][count] - 1
#             count2 = count
#         else: 
#             count = npr.randint(0,29)
#             count2 = 30
# 
# fixed it by the sampling function based on
# https://stackoverflow.com/questions/17821458/random-number-from-histogram

cars_data_base["Distance Driven"] = draw_from_hist(
    driven_distance_data["Average distance driven [km/day]"].to_numpy(),
    driven_distance_data["Number of cars"].to_numpy(),
    cfg.N,
    )


#### assign the cars to the grid nodes
# how many grid nodes?
G = len(grid)

car_distr = relative_assign(cfg.rel_car_distribution, cfg.N)
assert(sum(car_stat['Amount owned']) == cfg.N)

# get the array describing how many go to which city in another
# format so that it can be used for indexing. For instance:
# car_distr == [4 4 3]  --> car_alloc = [0 0 0 0 1 1 1 1 2 2 2]
# car_alloc = [k for k in range(G) for l in range(car_distr[k])]# ugly, slow
car_alloc = np.arange(G).repeat(car_distr) # cool, fast

# randomize which cars will be assigned
npr.shuffle(car_alloc)

# assign grid node name to cars_data_base
cars_data_base["GridConn"] = grid.index[car_alloc]

#### determine precise location of the cars
# loop over grid nodes
for index, row in grid.iterrows():
    # determine cars in this location
    car_bool = cars_data_base["GridConn"] == index
    
    # randomize coordinate locations:
    # we need:
    rad = row["2SigRadius"]           # 95.7% radius in m
    mu = row[["Long", "Lat"]].to_numpy().astype(float)  # coordinates
    
    # convert 2 sigma radius in m to degrees long and lat
    sx, sy = (rad/2  # convert 2 sigma to 1 sigma
        / (RE * np.pi/180  # one arc-degree on Earth's surface
            * np.array([np.cos(mu[1]*np.pi/180), # correct for parallels 
                                                 # getting shorter near poles
                        1])
              ))
    
    # covariance matrix with 0 correlation
    cov = np.diag(np.array([sx, sy])**2)
    
    # draw from multivariate normal
    cars_data_base.loc[car_bool, ["Long", "Lat"]]\
        = npr.multivariate_normal(mu, cov, size=sum(car_bool))
    
    
#### assign a random home charger based on the probabilities in SimConfig
cars_data_base["Charger type"] \
    = draw_from_hist([1, 2, 3, 4], cfg.p_home_charger_type,
                     cfg.N,
                     )

#%% car_data frame --> time dependent attributes

#### prepare new dataframe
# Repeat entries such that we have one per time slot per car
cars_data = cars_data_base.loc[
    cars_data_base.index.repeat(cfg.K)
    ].reset_index(drop=True)

# add timeslot integers for all cars
cars_data["Time"] = np.tile(np.arange(cfg.K).astype(int), cfg.N)
cars_data["Load"] = 0
cars_data["Charger Power"] = 0



#### find timeslots where we use home charger
# find index in timeslot array for end of morning, start of evening
morn_even_idx = np.searchsorted(cfg.t, [6, 18]) - 1

midday_bool = ((cars_data["Time"] > morn_even_idx[0])
                    & (cars_data["Time"] <= morn_even_idx[1]))

# assign wildcard charger for midday
cars_data.loc[midday_bool, "Charger type"] = -1

# some timeslots are blocked; we drive there, so we cannot charge:
time_data = change_hist_bins(driven_time_data["Share driven cars [%]"],
                             cfg.K,
                             )

cars_data.loc[(np.tile(time_data, cfg.N) > npr.random(cfg.N * cfg.K)*100),
              "Charger type",
              ] = 0

  
# make sure of datatypes    
cars_data = cars_data.astype({'Time': int,
                              'GridConn': str,
                              'Long': float,
                              'Lat': float,
                              'Charger type': int,
                              'Charger Power': int,
                              'Load': float,
                              })

    