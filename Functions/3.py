def func(l):
	sum=1
	for x in l:
		sum*=x
	return sum

l=[1,2,3,4,5]
print(func(l))