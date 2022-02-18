d={8:20, 2:40, 3:60, 1:50}
print(d)

for key in sorted(d):
	print("{} : {}".format(key,d[key]))