from collections import Counter

def func(filename):
	with open(filename) as f:
		return Counter(f.read().split())


print(func("demo.txt"))