dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 6:60}

for count, (key,value) in enumerate(dict_num.items(),1):
	print("{} {} {} ".format(key,value,count))