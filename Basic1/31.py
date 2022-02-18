x=int(raw_input("Num1: "))
y=int(raw_input("Num2: "))

if(x%y==0):
	gcd=y
elif(y%x==0):
	gcd=x
else:
	for i in range(y/2,0,-1):
		if(x%i==0 and y%i==0):
			gcd=i
			break

print(gcd)