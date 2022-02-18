from collections import Iterable

def func(lst):
  return ([a for i in lst for a in func(i)] if isinstance(lst, Iterable) else [lst])

print(func([1,[2,[3,4]],9]))
