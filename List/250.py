def func(lis,fn):
	return(sum(list(map(fn,lis))))


print(func([1,2,3,4,5,6,7,8],lambda x: x*2))