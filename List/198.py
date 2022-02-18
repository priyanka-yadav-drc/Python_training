nums1 = [1, 2, 3, 4, 5 ,6]
nums2 = [7, 8, 5, 2, 10, 12]

nums2=set(nums2)
print([i for i,el in enumerate(nums1) if el in nums2])