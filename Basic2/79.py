def func(nums):
    max_val = nums[0]

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                max_val = max(nums[i] * nums[j] * nums[k], max_val)
                
    return max_val
    
print(func([50,10,-2,4]))
print(func([-1, -2, 4, 2, 1]))
print(func([1, 2, 3, 4, 5, 6]))
