from copy import deepcopy

tuplex = ("HELLO", 5, [], True) 
print(tuplex)
new_tup=deepcopy(tuplex)

new_tup[2].append(80)
print(new_tup)