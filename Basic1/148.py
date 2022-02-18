def find_max(num):
	mini=num[0]
	maxi=num[0]

	for i in range(len(num)):
		if num[i]>maxi:
			maxi=num[i]
		if num[i]<mini:
			mini=num[i]
	return maxi,mini

lis=[2,6,1,8,55,30,100,-7]
print(lis)
print(find_max(lis))