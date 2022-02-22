def func(n,m):
	lis1=[]
	lis2=[]
	for i in range(1,n+1,1):
		if n%i==0:
			lis1.append(i)

	for j in range(1,m+1,1):
		if m%j==0:
			lis2.append(j)

	print("common divisors of {} and {} are:".format(n,m))
	for x in lis1:
		if x in lis2:
			print x, 
func(8,4)