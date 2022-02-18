lis=[1,2,2,6,4,8,4,6,1,8,7,9]

new_lis=[]

for x in lis:
	if x not in new_lis:
		new_lis.append(x)

print(lis)
print(new_lis)

for x in new_lis:
	print(lis.count(x))