x=2
cnt=input("enter n: ")
count=0

while x!=cnt:
	flag=0
	for i in range(2,x,1):
		if x%i==0:
			flag=1
			break

	if flag==0:
		count+=1

	x+=1

print(count)