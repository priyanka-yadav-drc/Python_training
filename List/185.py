num=5
result=[]
while num!=1:
	x=num%2
	result.append(x)
	num=num/2
result.append(num)
print(result[::-1])