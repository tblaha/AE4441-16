# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:59:41 2020

@author: timon
"""

"Attempting to read from LP solve file, modify & spit out a new (solvable) LP solve file"

#%% Reading the LP solve file, first practicing with textfile 

book = open("Original.LP", 'r') 
data = book.read()

#%% Deleting the first two text rows 

fullstops = list() 
iterations = list() 
for i in range(len(data)): 
    if len(fullstops) < 2: 
        if data[i] == '.':
            fullstops.append(data[i])
            iterations.append(i+2)

newdata1 = data[iterations[1]:]


#%%Next steps in cleanup process 


newdata2 = newdata1.replace("Minimize", "Min")
newdata3 = newdata2.replace("Subject To", ';')
newdata4 = newdata3.replace("End", ";") 
newdata5 = newdata4.replace("Bounds", '')

semicolons = list() 
iterations = list()
for j in range(len(newdata5)):
    if len(semicolons) < 1: 
      if newdata5[j] == ';':
          semicolons.append(newdata5[j])
          iterations.append(j)
 


         
'''steps still to be incorporated: 
    1. Put semicolun (;) after each constraint
    2. 
    3. 
    4.                                                  '''

#%%Writing to a new LP file called File1 

File1 = open("File1.LP", 'w')
File1.write(newdata5) 













