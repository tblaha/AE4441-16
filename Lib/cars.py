import pandas as pd
import numpy as np
import random

mtk = 1.609344
car_stat = pd.DataFrame({'Car Type': ['Tesla Model 3','Tesla Model Y','Tesla Model X', 'Chevy Bolt', 'Tesla Model S','NISSAN LEAF','Audi e-tron','BMW i3']} )
car_stat['Amount owned'] = [4000,2000,1000,1000,500,500,500,500]
car_stat['Battery size'] = [50,50,100,60,100,40,95,42.2]
car_stat['Range'] = [int(240*mtk),int(240*mtk),int(250*mtk),int(238*mtk),int(285*mtk),int(150*mtk),int(204*mtk),int(153*mtk)]
car_stat['kWh/km'] = car_stat['Battery size']/car_stat['Range']
entities = np.arange(0,sum(car_stat['Amount owned']))
current_entity = 0

cars_data = pd.DataFrame({'Car Type': entities, 'Distance Driven': entities, 'kWh/km': entities, 'Battery size': entities, 'Grid connection 1': entities, 'Grid connection 2': entities, 'Grid connection 3': entities, 'Grid connection 4': entities,'Charger type': entities})

for i in range(0,car_stat['Car Type'].size):
    cars_data.loc[ 
        current_entity:int(current_entity + car_stat['Amount owned'][i]),
        'Car Type'
        ] = car_stat['Car Type'][i]
    
    cars_data.loc[
        current_entity:int(current_entity + car_stat['Amount owned'][i]),
        'Battery size'
        ] = car_stat['Battery size'][i]
    
    current_entity = int(current_entity + car_stat['Amount owned'][i]) 

for i in range(0,sum(car_stat['Amount owned'])):
    cars_data.at[i, 'Distance Driven'] = random.randint(1,6)*10
    cars_data.at[i, 'kWh/km'] = random.randint(9,14)
    cars_data.at[i, 'Grid connection 1'] = int(random.randint(5,19)/10)
    cars_data.at[i, 'Grid connection 2'] = int(random.randint(0,15)/10)
    cars_data.at[i, 'Grid connection 3'] = int(random.randint(6,19)/10)
    cars_data.at[i, 'Grid connection 4'] = int(random.randint(0,19)/10)
    cars_data.at[i, 'Charger type'] = 1#random.randint(0,1)