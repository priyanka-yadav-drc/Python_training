nums = [1234, 122, 1984, 19372, 100]

result=all(str(x)[0] == str(nums[0])[0] for x in nums)
print(result)