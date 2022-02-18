list1=[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2,1,1,1]
max=0
for x in list1:
	if(max<list1.count(x)):
		max=list1.count(x)
		result=x

print(result)


