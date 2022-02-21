import re
x=True
count=0
pw=raw_input("enter password: ")
n=len(pw)
while x==True:
	if n<6 or n>16:
		print("if 1")
		break
	elif not re.search("[a-z]",pw):
		print("if 2")
		break
	elif not re.search("[A-Z]",pw):
		print("if 3")
		break
	elif not re.search("[0-9]",pw):
		print("if 4")
		break
	elif not re.search("[$#@]",pw):
		print("if 5")
		break
	#elif re.search("\s",pw):
	#	break
	else:
		print("Valid password")
		x=False
		break

if x:
	print("Invalid password")