dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}
print(dict1)

dict1={x:y for (x,y) in dict1.items() if y is not None}
print("new dictionary:")
print(dict1)