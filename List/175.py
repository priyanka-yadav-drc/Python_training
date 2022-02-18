nums = [(2,3),(2,4),(0,6),(7,1)]
print(zip(*nums))
result1 = map(max, zip(*nums))
result2 = map(min, zip(*nums))
print(result1)
print(result2)