def func(filename):
	with open(filename) as f:
		result=f.readlines()
	return result

print(func("demo.txt"))