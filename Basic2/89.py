def func(nums):
	nums.sort()
	sum=0
	for i in range(3):
		sum+=nums[i]

	return sum

print(func([7,2,4,3,8,9]))