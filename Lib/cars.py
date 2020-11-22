import pandas as pd
import numpy as np
import random

from Lib import SimConfig as cfg

#Random information
#https://ev-database.org/compare/efficiency-electric-vehicle-most-efficient#sort:path~type~order=.efficiency~number~asc|range-slider-range:prev~next=0~1200|range-slider-acceleration:prev~next=2~23|range-slider-topspeed:prev~next=110~450|range-slider-battery:prev~next=10~200|range-slider-eff:prev~next=100~300|range-slider-fastcharge:prev~next=0~1500|paging:currentPage=0|paging:number=9
#https://ev-sales.blogspot.com/2020/10/europe-september-2020.html
#%% Constants

mtk = 1.609344
bornholm_data = [19740,33.8,0.613,0.03]

# Amounts are estimated and the rest is public data
car_stat = pd.DataFrame({'Car Type': ['Renault Zoe','Tesla Model 3','VW e-Golf', 'Hyundai Kona', 'Audi e-Tron']} )
car_stat['Percentage owned'] = [32,28,16,12,12]
car_stat['Battery size'] = [52,47.5,32,39.2,64.7]
car_stat['Range'] = [315,320,190,255,280]
car_stat['kWh/km'] = car_stat['Battery size']/car_stat['Range']

for i in range(0,car_stat['Car Type'].size):
    car_stat.at[i,'Amount owned'] = int(car_stat['Percentage owned'][i]/100*cfg.N)
car_stat['Amount owned'][0] = car_stat['Amount owned'][0] + cfg.N - sum(car_stat['Amount owned'])

# Averages are taken from the fastned website and IEC - 61851-1
car_stat['Mode 4 175 kW'] = [41,105,39,35,115]
car_stat['Mode 4 50 kW'] = [41,45,39,35,50]
car_stat['Mode 2 3-phase'] = [22,11,7.2,11,11]
car_stat['Mode 2 1-phase'] = [7.4,7.4,7.2,7.4,7.4]

entities = np.arange(0,sum(car_stat['Amount owned']))
current_entity = 0
count2 = 30

# Averages are read from graphs of Bornholm
driven_distance_data = pd.DataFrame({'Average distance driven [km/day]': np.arange(0,150,5)})
driven_distance_data['Share of the cars [%]'] = [4,7,12,11,11,9,10,6,5,3,4,2,3,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0]
for i in range(0,driven_distance_data['Average distance driven [km/day]'].size):
    driven_distance_data.at[i, 'Number of cars'] = int(driven_distance_data['Share of the cars [%]'][i]/100*bornholm_data[0])

# Averages are read from graphs of Bornholm
driven_time_data = pd.DataFrame({'Time of day [h]': np.arange(0,24)})
driven_time_data['Share driven cars [%]'] = [0,0,0,0,0,1,3,5,3,3,4,4,4,4,4,6,7,5,3,2,1,2,1,0]


#%% Dataset per car
time_data= []

for j in range(0,cfg.K):
    time_data.append(sum(driven_time_data['Share driven cars [%]'][int(j*24/cfg.K):int((j+1)*24/cfg.K)]))


cars_data = pd.DataFrame({'Car Type': entities, 'Distance Driven': entities, 'Battery size': entities, 'kWh/km': entities, 'Mode 4 175 kW': entities, 'Mode 4 50 kW': entities, 'Mode 2 3-phase': entities, 'Mode 2 1-phase': entities})
# The cars are put in a new DataFrame one on each row based on the car_stat
for i in range(0,car_stat['Car Type'].size):
    cars_data.loc[ 
        current_entity:int(current_entity + car_stat['Amount owned'][i]),
        'Car Type'
        ] = car_stat['Car Type'][i]
    
    cars_data.loc[
        current_entity:int(current_entity + car_stat['Amount owned'][i]),
        'Battery size'
        ] = car_stat['Battery size'][i]

    cars_data.loc[
        current_entity:int(current_entity + car_stat['Amount owned'][i]),
        'kWh/km'
        ] = car_stat['kWh/km'][i]

    cars_data.loc[
        current_entity:int(current_entity + car_stat['Amount owned'][i]),
        'Mode 4 175 kW'
        ] = car_stat['Mode 4 175 kW'][i]

    cars_data.loc[
        current_entity:int(current_entity + car_stat['Amount owned'][i]),
        'Mode 4 50 kW'
        ] = car_stat['Mode 4 50 kW'][i]

    cars_data.loc[
        current_entity:int(current_entity + car_stat['Amount owned'][i]),
        'Mode 2 3-phase'
        ] = car_stat['Mode 2 3-phase'][i]

    cars_data.loc[
        current_entity:int(current_entity + car_stat['Amount owned'][i]),
        'Mode 2 1-phase'
        ] = car_stat['Mode 2 1-phase'][i]
    
    current_entity = int(current_entity + car_stat['Amount owned'][i]) 





cars_t_data = pd.DataFrame({'Car Type': entities, 'Distance Driven': entities, 'Battery size': entities, 'kWh/km': entities, 'Mode 4 175 kW': entities, 'Mode 4 50 kW': entities, 'Mode 2 3-phase': entities, 'Mode 2 1-phase': entities, 'Grid slot': entities, 'Grid availability': entities})

for i in range(0,cars_data['Car Type'].size):

# The distance driven by a car is randomly assigned from the driven_distance_data. This does not work perfectly as whole percentages are used in the original data
    count = random.randint(0,29)
    while count != count2:
        if driven_distance_data['Number of cars'][count] > 0:     
            cars_data.at[i, 'Distance Driven'] = driven_distance_data['Average distance driven [km/day]'][count]
            driven_distance_data['Number of cars'][count] = driven_distance_data['Number of cars'][count] - 1
            count2 = count
        else: 
            count = random.randint(0,29)
            count2 = 30

    

# Still work in progress
    cars_data.at[i, 'Charger type'] = 1#random.randint(0,1)
    

    for j in range(0,cfg.K):
        cars_t_data.loc[ 
            int(i*cfg.K+j),
            'Car Type'
            ] = cars_data['Car Type'][i]

        cars_t_data.loc[
            int(i*cfg.K+j),
            'Distance Driven'
            ] = cars_data['Distance Driven'][i]
        
        cars_t_data.loc[
            int(i*cfg.K+j),
            'Battery size'
            ] = cars_data['Battery size'][i]
    
        cars_t_data.loc[
            int(i*cfg.K+j),
            'kWh/km'
            ] = cars_data['kWh/km'][i]
    
        cars_t_data.loc[
            int(i*cfg.K+j),
            'Mode 4 175 kW'
            ] = cars_data['Mode 4 175 kW'][i]
    
        cars_t_data.loc[
            int(i*cfg.K+j),
            'Mode 4 50 kW'
            ] = cars_data['Mode 4 50 kW'][i]
    
        cars_t_data.loc[
            int(i*cfg.K+j),
            'Mode 2 3-phase'
            ] = cars_data['Mode 2 3-phase'][i]
    
        cars_t_data.loc[
            int(i*cfg.K+j),
            'Mode 2 1-phase'
            ] = cars_data['Mode 2 1-phase'][i]
        
        cars_t_data.loc[
            int(i*cfg.K+j),
            'Grid slot'
            ] = j+1
        
        cars_t_data.loc[
            int(i*cfg.K+j),
            'Grid availability'
            ] = int(2 - random.random() - time_data[j]/100)  
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    