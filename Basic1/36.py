def func(x,y):
	z=4
	if type(x)==type(y)==type(z):
		return x+y
	else:
		return "cannot add"
print(func(3,8))