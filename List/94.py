lis=[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
result=[]
for x in lis:
	if lis.count(x)==1:
		result.append(x)

print(result)