def func(n):
	result=[]

	while n!=1:
		result.append(n%2)
		n=n/2
	result.append(n)
	num=0
	j=0
	for i in reversed(range(len(result))):
		num+=(result[i]*(2**j))
		j+=1
	return num

print(func(13))
