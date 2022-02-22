def func(nums,n):
	for x in range(len(nums)):
		for y in range(x+1,len(nums)):
			if nums[x]+nums[y]==n:
				return True
	return False

lis=[1,2,3,4,5]
print(func(lis,6))
print(func([6,7,5,4],4))