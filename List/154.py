nums1 = [[10,20], [30,40], [50,60], [30,20,80]]
nums2 = [[61], [12,14,15], [12,13,19,20], [12]]

result=[x+y for x, y in zip(nums1,nums2)]
print(result)