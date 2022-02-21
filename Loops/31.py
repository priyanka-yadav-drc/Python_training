age1=input("enter dog's age in human years: ")

if age1<0:
	print("Age should be positive.")
	exit()
elif age1<=2:
	age2=age1*10.5
else:
	age2=(age1-2)*4+21

print("dog's age in dog years: {}".format(age2))
