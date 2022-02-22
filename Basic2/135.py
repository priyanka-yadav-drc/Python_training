from functools import reduce

def func(nums):
	return reduce(lambda x,y:lcm(x,y), nums )

def gcd(x,y):
	while y:
		x,y=y,x%y
	return x

def lcm(x,y):
	return x*y//gcd(x,y)

print(func([10,25,30]))
print(func([1,2,3,4,5,6]))