d={1:20, 2:40, 3:60}
print(d)

if 1 in d:
	del d[1]

print("after deleting {}".format(d))