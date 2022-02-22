def func(nums):
	result=[0,0]
	for x in nums:
		if x<0:
			result[0]+=x
		else:
			result[1]+=x

	return result

print(func([-2,-4,5,1,-6]))