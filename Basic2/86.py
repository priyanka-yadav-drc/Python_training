def func(x, y, z):
  result= set([x, y, z])
  if len(result)==3:
    return 0
  else:
    return (4 - len(result))

print(func(1, 1, 1))
print(func(1, 2, 2))
print(func(1,2,3))

