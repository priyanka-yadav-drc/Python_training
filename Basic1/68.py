n=int(raw_input("Enter num: "))

result=0
while n!=0:
	n1=n%10
	result=result+n1
	n=n/10

print(result)