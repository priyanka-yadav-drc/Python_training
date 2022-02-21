x=input("enter x: ")
y=input("enter y: ")
z=input("enter z: ")

if x==y==z:
	print("Equilateral triangle.")
elif x==y or y==z or x==z:
	print("isoceles triangle.")
else:
	print("scalene triangle")