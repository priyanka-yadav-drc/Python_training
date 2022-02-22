def func(nums):
	n=len(nums)
	sum=0
	for x in nums:
		sum+=x

	if sum%n==0:
		return True
	else:
		return False

print(func([1,2,3,4]))
print(func([1,2,3]))