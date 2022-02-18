nums=[2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
print(nums)
sum=0
l=10
r=20
for x in nums:
	if x>=l and x<=r:
		sum+=x

print(sum)