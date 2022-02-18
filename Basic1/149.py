def func(n):
	n=n-1
	result=0
	while n!=0:
		result= result+(pow(n,3))
		n=n-1
	return result

print(func(8))