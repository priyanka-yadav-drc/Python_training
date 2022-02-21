print("Input some integers to calculate their sum and average. Input 0 to exit.")

count = 0
sum = 0.0
number = 1

while number!=0:
	number=int(input(""))
	sum+=number
	count+=1

if count==0:
	print("no numbers entered.")
else:
	print("sum={} and average={}".format(sum, sum/(count-1)))