def func(n,m):
	x=str(n)
	y=str(m)
	sum=0
	for i,j in zip(x,y):
		z=abs(int(i)-int(j))
		sum+=z

	return sum

print(func(123,256))
print(func(170,657))