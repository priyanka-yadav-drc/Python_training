def func(n):
	temp=str(n)
	while n>0:
		n=n-sum([int(i) for i in temp])
		temp=list(str(n))
	return n

print(func(20))
print(func(167))