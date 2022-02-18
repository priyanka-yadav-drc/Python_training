d={1:20, 2:40, 3:60}
prod=1
print(d)

for key in d:
	prod*=d[key]

print("product={}".format(prod))