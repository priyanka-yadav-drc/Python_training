def func(test,fn):
	return(dict(zip(test,map(fn,test))))

print(func([1,2,3,4,5,6], lambda x:x**2))