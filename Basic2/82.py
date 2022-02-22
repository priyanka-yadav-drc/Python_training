def func(nums):
	n=len(nums)
	nums.sort()
	m=n//2

	if n%2==0:
		return float(nums[m-1]+nums[m])/2
	else:
		return nums[m]

print(func([1,2,3,4,5,6]))
print(func([9,2,4,3,5]))