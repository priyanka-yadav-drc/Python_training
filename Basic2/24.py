def func(n):
	count=0
	for i in range(1,n+1,1):
		if n%i==0:
			count+=1

	if count%2==0:
		return "even number of divisors"
	else:
		return "odd number of divisors"

print(func(15))