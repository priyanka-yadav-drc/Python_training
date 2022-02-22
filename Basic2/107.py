def func(num):
	s=str(num)
	sum=0
	for x in s:
		sum+=int(x)
	if sum%2==0:
		return "evenish"
	else:
		return "oddish"

print(func(34))
print(func(11))