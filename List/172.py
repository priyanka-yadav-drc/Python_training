l1=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
n=2
for x in range(len(l1)-1,len(l1)-1-n,-1):
	l1.pop(x)

print(l1)