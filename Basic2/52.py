x=2
cnt=input("enter how many prime numbers: ")
count=0
sum=0
while count!=cnt:
	flag=0
	for i in range(2,x,1):
		if x%i==0:
			flag=1
			break

	if flag==0:
		count+=1
		sum=sum+x

	x+=1

print(sum)


