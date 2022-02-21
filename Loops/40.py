a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))

lis=a,b,c

lis2=sorted(lis)

print("median= {}".format(lis2[1]))