n=int(raw_input("Enter a number : "))
if(abs(1000-n)<=100 or abs(2000-n)<=100) :
	print("Yes the given number is within 100 of 1000 or 2000")
else :
	print("No the given number is not within 100 of 1000 or 2000")