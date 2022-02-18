list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

d=raw_input("Enter direction left or right: ")
n=input("Enter how many positions to move: ")

if d=="left":
	result=list1[n:]+list1[:n]
elif d=="right":
	result=list1[-n:]+list1[:-n-1]

print(result)