lis=[1,4,2,3,6,0,9]
result=[]
i=0
j=1
while i<len(lis)-1 and j<len(lis):
		result.append(lis[j]-lis[i])
		i+=1
		j+=1


print(result)