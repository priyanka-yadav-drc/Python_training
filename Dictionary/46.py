colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
result={}
for x,y in colors:
	result.setdefault(x,[]).append(y)

print(result)
