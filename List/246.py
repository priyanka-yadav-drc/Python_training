def some(lst, fn = lambda x: x):
  return any(map(fn, lst))
print(some(['white','red','pink'], lambda x: len(x) > 3))
print(some(['white','red','pink'], lambda x: len(x) < 3))