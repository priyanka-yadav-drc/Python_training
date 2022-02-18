from itertools import combinations

list1=['orange', 'red', 'green', 'blue']
result=[]
for x in range(len(list1)):
	result.append(list(combinations(list1,x))
print(result)