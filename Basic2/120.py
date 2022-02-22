def gcd(x,y):
	while y!=0:
		x,y=y,x%y
	return x

def coprime(x,y):
	return gcd(x,y)==1

def func(x):
	if x==1:
		return 1
	else:
		result= [i for i in range(1,x) if coprime(i,x)]
		return len(result)

print(func(10))