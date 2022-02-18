def func(lis,weight):
	return(sum(x*y for x,y in zip(lis,weight))/sum(weight))

nums1 = [82, 90, 76, 83]
nums2 = [.2, .35, .45, 32]

print(nums1)
print(nums2)
print(func(nums1,nums2))
