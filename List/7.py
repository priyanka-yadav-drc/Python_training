lis=[1,2,2,6,4,8,4]

new_lis=[]

for x in lis:
	if x not in new_lis:
		new_lis.append(x)

print(lis)
print(new_lis)