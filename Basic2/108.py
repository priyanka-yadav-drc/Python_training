def func(x,y,z):
	a=str(x)
	b=str(y)
	c=str(z)

	if int(a[-1])*int(b[-1])==int(c[-1]):
		return True
	else:
		return False

print(func(22,12,34))
print(func(23,14,71))