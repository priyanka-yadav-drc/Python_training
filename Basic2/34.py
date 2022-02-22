print("Input three integers(sides of a triangle)")
int_num = list(map(int,raw_input().split()))

a,b,c=sorted(int_num)

if a**2 + b**2 == c**2:
	print("It is a right angle triangle")
else:
	print("It is not a right triangle")