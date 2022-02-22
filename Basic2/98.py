def func(nums):
	return all([nums[i]>nums[i-1] for i in range(1,len(nums),1)])

print(func([1,2,3,4,5]))
print(func([1,4,3,7]))