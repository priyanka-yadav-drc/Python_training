n=input("Enter no of lines: ")
if n<=0:
	print("Lines<=0")
else:
	print("No of regions: {}".format((n*n+n+2)//2))