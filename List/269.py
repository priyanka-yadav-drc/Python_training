lis=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=[]
print(lis)
n=input("enter n: ")
for i in range(len(lis)):
	if i%(n)==0:
		result.append(lis[i])

print(result)