def func(filename):
	with open(filename) as f:
		words=f.read().split()
	max_len=len(max(words,key=len))
	return [word for word in words if len(word)==max_len]

print(func("demo.txt"))