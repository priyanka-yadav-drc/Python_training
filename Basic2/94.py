def func(nums):
	return max([nums[i-1]*nums[i] for i in range(1,len(nums),1)])

print(func([1,2,3,4,5]))
print(func([9,7,3,2]))