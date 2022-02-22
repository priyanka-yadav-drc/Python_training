x = input("Input the first number")
y = input("Input the second number")
z = input("Input the third number")

lis=x,y,z

num=list(sorted(lis))

print("median is= {}".format(num[1]))

