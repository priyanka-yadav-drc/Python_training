def func(nums):
	sum=0
	for i in range(len(nums)):
		sum+=(i*nums[i])

	return sum

print(func([1,2,3,4]))
print(func([1,1,1]))