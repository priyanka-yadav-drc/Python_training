lis=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
result=dict()
for d in lis:
	for x,y in d.items():
		result.update({x:int(y)})

print(result)