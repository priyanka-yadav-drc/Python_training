nums = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print(nums)
nums=list(map(round,nums))
print("min num: {}".format(min(nums)))
print("max num: {}".format(max(nums)))
nums=list(set(nums))
for i in range(len(nums)):
	nums[i]=nums[i]*5

print(nums)
