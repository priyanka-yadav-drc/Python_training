from collections import defaultdict

colors = ['Red', 'Green', 'Black', 'White', 'Pink']
d=defaultdict(list)
for x in colors:
	d[len(x)].append(x)

print(dict(d))