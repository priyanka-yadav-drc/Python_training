lis1=['Red color', 'Orange#', 'Green', 'Orange @', 'White']
lis2=['#', 'color', '@']
result=[]
flag=0
for x in lis1:
	flag=0
	for y in lis2:
		if y in x:
			flag=1
			break

	if (flag==0):
		result.append(x)

print(lis1)
print(lis2)
print("result: {}".format(result))