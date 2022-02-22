def func(lis1,lis2):
	return all([ch in lis1.lower() for ch in lis2.lower()])

print(func('priyanka','priya'))
print(func('hello','hi'))