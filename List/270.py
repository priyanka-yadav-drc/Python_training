def func(lsts, nums):
  for x in lsts:
    if x not in nums:
      return False
  return True
print(func([1,2,3], [4,5,2,3,6,1]))