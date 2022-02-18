def func(filename,n):
	with open(filename) as f:
		for line in (f.readlines()[-n:]):
			print(line)

func("demo.txt",2)