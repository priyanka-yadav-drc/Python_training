lis=[0,1,2,3,4,5]
print(lis)
for i in range(len(lis)):
	if i%2==0:
		x=lis[i]
		lis[i]=lis[i+1]
		lis[i+1]=x


print(lis)