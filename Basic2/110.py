def func(nums):
	return [x for x in nums if nums.count(x)==1]

print(func([1,2,2,3,4,3,5]))