def func(n):
	y=0
	while n>0:
		n=n/5
		y=y+n
	return y

print(func(100))