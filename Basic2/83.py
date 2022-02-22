def func(num):
	if str(num)==str(num)[::-1]:
		return "symmetrical"
	else:
		return "not symmetrical"

print(func(12321))
print(func(1000))