print("Input first integer:")
x = int(input())
print("Input second integer:")
y = int(input())

if(len(str(x+y))>80):
	print("overflow!")
else:
	print(x+y)