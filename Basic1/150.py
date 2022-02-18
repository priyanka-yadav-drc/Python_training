def func(num):
	for i in range(len(num)):
		for j in range(len(num)):
			if i!=j:
				prod=num[i]*num[j]
				if prod%2!=0:
					return True
	return False


print(func([1,4,8]))