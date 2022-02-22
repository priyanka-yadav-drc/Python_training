def func(n):
	if(n==1 or n==2 or n==3 or n==4):
		return 1
	else:
		return func(n-1)+func(n-2)+func(n-3)+func(n-4)


print(func(5))
print(func(6))
print(func(7))
print(func(8))
print(func(9))