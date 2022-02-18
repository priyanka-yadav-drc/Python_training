def func(n):
	prod=1
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		while n>0:
			prod=prod*n
			n-=1
		return prod

print(func(6))