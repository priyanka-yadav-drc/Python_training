color_dict = {1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}

result={}

for x in color_dict.values():
	result[x]=len(x)

print(result)