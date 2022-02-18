def func(lis,n):
	return(lis[-n:]+lis[:-n])

result=func([6,7,8,4,5,1,2,3],3)
print(result)