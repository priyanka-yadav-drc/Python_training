l1 = [1,1,2,3,3,4,4,5,6,7]
l2 = [1,1,2,4,5,6]
result=list(l1)

for x in l2:
	result.remove(x)
print(result)
