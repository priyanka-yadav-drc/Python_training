def func(n):
	x = n
	y = n
	while True:
		if str(x) == str(x)[::-1]:
			return x
		x -=  1
		if str(y) == str(y)[::-1]:
			return y
		y += 1
	return int(bin(n)[::-1][:-2], 2)

print(func(120))
