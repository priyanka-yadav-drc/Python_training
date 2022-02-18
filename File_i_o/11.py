import os
def func(filename):
	statinfo = os.stat(filename)
	return statinfo.st_size

print(func("demo.txt"))