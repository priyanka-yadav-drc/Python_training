import time
def func():
	start=time.time()
	x=100000000
	y=700000000000
	sum=x+y
	print(sum)
	end=time.time()
	return end-start

print(func())