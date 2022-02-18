def func(n,low,up):
	if n in range(low,up+1):
		return True
	else:
		return False

print(func(20,10,50))