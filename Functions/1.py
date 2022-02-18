def max2(x,y):
	if x>y:
		return x
	return y

def max3(x,y,z):
	return max2(x,max2(y,z))

print("x:{} y:{} z:{}, max:{}".format(99,102,34,max3(99,102,34)))