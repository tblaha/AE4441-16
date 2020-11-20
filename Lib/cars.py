import pandas as pd
import numpy as np
import random

mtk = 1.609344
bornholm_data = [19740,33.8,0.613,0.03]
car_stat = pd.DataFrame({'Car Type': ['Tesla Model 3','Tesla Model Y','Tesla Model X', 'Chevy Bolt', 'Tesla Model S','NISSAN LEAF','Audi e-tron','BMW i3']} )
car_stat['Amount owned'] = [8000,4000,2000,2000,1000,1000,1000,740]
car_stat['Battery size'] = [50,50,100,60,100,40,95,42.2]
car_stat['Range'] = [int(240*mtk),int(240*mtk),int(250*mtk),int(238*mtk),int(285*mtk),int(150*mtk),int(204*mtk),int(153*mtk)]
car_stat['kWh/km'] = car_stat['Battery size']/car_stat['Range']
entities = np.arange(0,sum(car_stat['Amount owned']))
current_entity = 0
count2 = 30

driven_distance_data = pd.DataFrame({'Average distance driven [km/day]': np.arange(0,150,5)})
driven_distance_data['Share of the cars [%]'] = [4,7,12,11,11,9,10,6,5,3,4,2,3,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0]

for i in range(0,driven_distance_data['Average distance driven [km/day]'].size):
    driven_distance_data.at[i, 'Number of cars'] = int(driven_distance_data['Share of the cars [%]'][i]/100*bornholm_data[0])

driven_time_data = pd.DataFrame({'Time of day [h]': np.arange(0,24)})
driven_time_data['Share driven cars [%]'] = [0,0,0,0,0,1,3,5,3,3,4,4,4,4,4,6,7,5,3,2,1,2,1,0]

beun_time = [0,1/3,11/3,11/3,4,6,2,1]


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
    count = random.randint(0,29)
    while count != count2:
        if driven_distance_data['Number of cars'][count] > 0:     
            cars_data.at[i, 'Distance Driven'] = driven_distance_data['Average distance driven [km/day]'][count]
            driven_distance_data['Number of cars'][count] = driven_distance_data['Number of cars'][count] - 1
            count2 = count
        else: 
            count = random.randint(0,29)
            count2 = 30
    cars_data.at[i, 'kWh/km'] = random.randint(9,14)
    cars_data.at[i, 'Grid connection 1'] = int(2 - random.random() - beun_time[0]/100)
    cars_data.at[i, 'Grid connection 2'] = int(2 - random.random() - beun_time[1]/100)
    cars_data.at[i, 'Grid connection 3'] = int(2 - random.random() - beun_time[2]/100)
    cars_data.at[i, 'Grid connection 4'] = int(2 - random.random() - beun_time[3]/100)
    cars_data.at[i, 'Grid connection 5'] = int(2 - random.random() - beun_time[4]/100)
    cars_data.at[i, 'Grid connection 6'] = int(2 - random.random() - beun_time[5]/100)
    cars_data.at[i, 'Grid connection 7'] = int(2 - random.random() - beun_time[6]/100)
    cars_data.at[i, 'Grid connection 8'] = int(2 - random.random() - beun_time[7]/100)
    cars_data.at[i, 'Charger type'] = 1#random.randint(0,1)