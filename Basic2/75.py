def func(nums,n):
	for x in nums:
		if x==n:
			nums.remove(x)
	print(nums)
	return len(nums)

print(func([1,4,2,4],4))