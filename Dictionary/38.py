x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 3}

for key, value in set(x.items()) & set(y.items()):
	print("{}:{} is present in both dictionaries".format(key,value))