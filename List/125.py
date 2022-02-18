nums= [10, 20, 30, 40, 20, 50, 60, 40]
nums2=list(set(nums))
result=1
for x in nums2:
		result=result*x

print(result)
