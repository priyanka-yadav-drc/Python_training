def func(lis):
	result=[]
	for x in lis:
		if x not in result:
			result.append(x)
	return result

print(func([1,2,3,3,3,3,4,5]))