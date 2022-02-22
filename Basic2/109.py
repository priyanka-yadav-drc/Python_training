def func(lis,num):
	result=[]
	for i in range(len(lis)):
		if lis[i]==num:
			result.append(i)

	return result

print(func([1,2,3,2,4,2],2))