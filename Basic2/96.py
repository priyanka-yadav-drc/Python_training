def func(n):
	l=len(str(n))
	n1=str(n)
	sum=0
	for x in n1:
		sum+=(int(x)**l)

	if sum==n:
		return True
	else:
		return False

print(func(153))
print(func(407))
print(func(409))

