def func(val):
	return(list(val) if isinstance(val,(tuple,set,list,dict)) else [val])

print(func({1,2,3}))
print(func([5,6,7,8]))
print(func(4))