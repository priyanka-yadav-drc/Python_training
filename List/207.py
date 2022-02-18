list1 =  [('red', 'green'), ('black', 'white'), ('orange', 'pink')] 
list2 =  [('red', 'green'), ('orange', 'pink')] 
result=set(list1).intersection(list2)
print(list(result))