lis={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
result=dict()

for x,y in lis.items():
		result.update({x:[]})

print(result)