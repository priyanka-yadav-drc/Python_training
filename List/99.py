list_val = ['Python', 3, 2, 4, 5, 'version'] 
max_val=max(i for i in list_val if isinstance(i,int))
min_val=min(i for i in list_val if isinstance(i,int))
print(max_val)
print(min_val)