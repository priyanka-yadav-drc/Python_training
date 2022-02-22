def func(lis):
	for i in range(len(lis)):
	 for j in range(len(lis)):
		if i!=j:
			if lis[i]==lis[j]:
				return False
	return True

lis=[2,5,4,7,8]
print(func(lis))