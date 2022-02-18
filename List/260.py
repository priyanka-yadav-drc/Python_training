def func(nums, lsts):
  for x in lsts:
    if x not in nums:
      return False
  return True
print(func(['a','b','c','x','y'], ['x','y']))