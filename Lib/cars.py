import pandas as pd
import numpy as np
import random

mtk = 1.609344
car_stat = pd.DataFrame(
    {'Car Type': ['Tesla Model 3','Tesla Model Y','Tesla Model X','Chevy Bolt',
                  'Tesla Model S','NISSAN LEAF','Audi e-tron','BMW i3'
                  ]}
    )
car_stat['Battery size'] = [50, 50, 100, 60, 100, 40, 95, 42.2]
car_stat['Range'] = mtk * np.array([240, 240, 250, 238, 285, 150, 204, 153])
car_stat['kWh/km'] = car_stat['Battery size']/car_stat['Range']

car_stat['Amount owned'] = [2, 1, 1, 0, 0, 0, 0, 1]

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

                
                
                