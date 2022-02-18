nums =  [1,2,3,4,5]

result=[[nums[i],nums[i+1]] for i in range(len(nums)-1)]
print(result)