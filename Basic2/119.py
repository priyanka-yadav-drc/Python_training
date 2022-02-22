def gcd(x,y):
	while y!=0:
		x,y=y,x%y
	return x

def func(x,y):
	return gcd(x,y)==1

print(func(17,18))
print(func(25,9))
print(func(20,40))