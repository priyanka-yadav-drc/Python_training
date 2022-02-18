ls=[6,1,4,8]
i=0
for i in range(len(ls)):
	j=0
	result=""
	while j<ls[i] :
		result=result+"@"
		j+=1
	print(result)