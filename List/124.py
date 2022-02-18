nums=[(2, 7), (2, 6), (1, 8), (4, 9)]
result_max = max([abs(x * y) for x, y in nums] )
result_min = min([abs(x * y) for x, y in nums] )
print(result_min)
print(result_max)