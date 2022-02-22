def func(n):
	if n==1:
		return [0,1]
	if n==0:
		return [1,0]
	result=[0,0]
	while n!=1:
		if n%2==0:
			result[0]+=1
		else:
			result[1]+=1
		n=n/2
	result[1]+=1
	return result

print(func(12))
print(func(1234))

