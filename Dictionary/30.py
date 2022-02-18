from operator import itemgetter
from heapq import nlargest

item = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for key,value in nlargest(3, item.items(), key=itemgetter(1)):
	print(key,value)
