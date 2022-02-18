lis=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(lis)
new_lis=[]
for i in range(len(lis)):
	if(i not in [0,4,5]):
		new_lis.append(lis[i])

print(new_lis)