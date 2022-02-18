def func(lis):
	result=[]
	for x in lis:
		if x%2==0:
			result.append(x)
	return result

print(func([1,2,3,4,5,6,7,8,9,10]))