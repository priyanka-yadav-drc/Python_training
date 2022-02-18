lis=[1, 2, 3, 4, 5, 6, 7]
result=[]
for i in range(len(lis)-1):
	z=(lis[i] + lis[i+1])
	z=float(z)/2
	print(z)
	result.append(z)

print(result)