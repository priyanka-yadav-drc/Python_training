def func(nums):
	sum=0
	result=[]
	for x in nums:
		sum+=x
		result.append(sum)
	return result

print(func([10,20,30,40]))
print(func([7,8,3,2,10]))