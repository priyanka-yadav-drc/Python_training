import itertools
def func(lst):
  return list(itertools.accumulate(lst))

print(func([4,5,6,7,8]))