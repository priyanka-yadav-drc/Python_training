def test(lst, fn = lambda x: x):
  return any(not fn(x) for x in lst)
print(test([1, 0, 2, 3], lambda x: x % 3==0 ))

