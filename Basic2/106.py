def func(num):
	return len(set(str(num)))==10

print(func(1023456789))
print(func(123456))