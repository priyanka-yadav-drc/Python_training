nums = ['1','2','3','4','5','6','7','8']

result=[x+y for x,y in zip(nums[::2],nums[1::2])]

print(result)