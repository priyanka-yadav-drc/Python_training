def func(num):
	res=True
	i=1
	n,temp=2,2
	while res:
		if str(temp) in num:
			i+=1
			temp=pow(n,i)
		else:
			res=False

	return i-1

print(func("24816"))