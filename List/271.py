def func(lis):
	for x in lis:
		if lis.count(x)>1:
			return False
	return True


lis=[1, 2, 3, 4, 5, 6, 7]
print(lis)

print(func(lis))
