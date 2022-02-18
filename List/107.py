list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(list1)
n=1
for i in list1:
	del i[n]

print(n)
print(list1)