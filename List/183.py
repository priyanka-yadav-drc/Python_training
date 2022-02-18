l1=[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
result=[]
for x in l1:
	for i in  x:
		if i not in result:
			result.append(i)
print(result)