nums = [12,33,23,10,67,89,45,667,23,12,11,10,54]
min_val=min(nums)
max_val=max(nums)

min_index=[i for i, j in enumerate(nums) if j==min_val]

max_index=[i for i, j in enumerate(nums) if j==max_val]
print(min_index)
print(max_index)