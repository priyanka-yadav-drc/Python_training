s=raw_input("enter the string: ")
d=l=0

for x in s:
	if x.isdigit()==True:
		d+=1
	elif x.isalpha()==True:
		l+=1

print("digits={}, letter={}".format(d,l))