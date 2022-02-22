def func(n):
	result=[]

	for x in range(1,n+1,1):
		if n%x==0:
			result.append(x)

	return result

print(func(8))
print(func(100))