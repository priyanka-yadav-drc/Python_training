str1=raw_input("enter a string: ")
str1=str1.strip()

if len(str1)<1:
	print("enter a valid text: ")
elif(all(x in "012345678" for x in str1)):
	print("it is integer")
else :
	print("it is string")