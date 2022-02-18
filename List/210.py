lis=[3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]
result=[]
j=0
res=0
for i in range(len(lis)):
	if lis[i]!=0:
		res=res+lis[i]
	else:
		j=j+1
		if lis[i-1]!=lis[i]:
			result.append(res)
		res=0
print(lis)
print(result)