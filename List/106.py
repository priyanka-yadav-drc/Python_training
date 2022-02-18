lis=[1, 'abcd', 3, 1.2, 4, 'xyz', 'pqr', 7, -5, -12.22]
count=0
for x in lis:
	if isinstance(x,int):
		count+=1

print(lis)
print(count)