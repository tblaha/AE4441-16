# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:59:41 2020

@author: timon
"""

"Attempting to read from LP solve file, modify & spit out a new (solvable) LP solve file"

import fileinput

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


newdata2 = newdata1.replace("Minimize", "min")
newdata3 = newdata2.replace("Subject To", ';')
newdata4 = newdata3.replace("Bounds", '')
newdata5 = newdata4.replace("Binaries", 'binary')
newdata6 = newdata5.replace("End", ";") 


semicolons = list() 
iterations = list()
for j in range(len(newdata5)):
    if len(semicolons) < 1: 
      if newdata6[j] == ';':
          semicolons.append(newdata6[j])
          iterations.append(j)
 
    

# check each line for a = character. If exists; append ";" to the line
# 
# just to be clear; this is beuncode if there ever was one... It would have 
# been much nicer if we had used "fileinput"
# https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file#
# this would have allowed working with "book" (which is a line-iterator in 
# itself) instead of looping through each and every character.
found = False
newdata7 = []
for j in range(len(newdata6)):
    if newdata6[j] == "=":
        # start new count, if we find "="
        found = True
    if (newdata6[j] == "\n") and found:
        # prepend a ; to the first line break "\n" after a "="
        found = False
        newdata7.append(";\n")
    else:
        newdata7.append(newdata6[j])

newdata8 = "".join(newdata7)
         


'''steps still to be incorporated: 
    1. Put semicolun (;) after each constraint
    2. 
    3. 
    4.                                                  '''

#%%Writing to a new LP file called File1 

book.close()
File1 = open("File1.LP", 'w')
File1.write(newdata8) 
File1.close()













