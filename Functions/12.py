def func(str):
	if str==str[::-1]:
		return True
	else:
		return False

print(func("madam"))
print(func("hello"))