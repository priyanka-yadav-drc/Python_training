def func(filename):
	result=[]
	with open(filename) as f:
		for line in f.readlines():
			result.append(line)
	return result

print(func("demo.txt"))