direct=raw_input("enter direction: ")
n=input("enter n : ")
lis=[1,2,3,4,5]
print(lis)

if direct=="left":
	print(lis[n:])
elif direct=="right":
	print(lis[:-n])