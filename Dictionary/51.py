dictionary = { 
               'Math' : [88, 89, 90], 
               'Physics' : [92, 94, 89],
               'Chemistry' : [90, 87, 93]
             }
dictionary['Math']=[x+2 for x in dictionary['Math']]

print(dictionary)