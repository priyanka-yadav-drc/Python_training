def func(nums):
	for i in range(len(nums)):
		if (i%2==0 and nums[i]%2==0) or (i%2==1 and nums[i]%2==1):
			pass
		else:
			return False
	return True

print(func([2,1,4,3]))
print(func([2,1,4,3,5]))