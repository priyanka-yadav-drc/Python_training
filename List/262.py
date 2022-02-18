def func(lis,n):
	return(lis[n:]+lis[:n])

result=func([6,7,8,1,2,3,4,5],3)
print(result)