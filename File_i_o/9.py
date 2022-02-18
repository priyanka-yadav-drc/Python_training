def func(filename):
	with open(filename) as f:
		for i,l in enumerate(f):
			pass

	return i+1

print(func("demo.txt"))