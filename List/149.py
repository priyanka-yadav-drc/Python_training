from itertools import combinations

lis=['orange', 'red', 'green', 'blue']

result=[combinations(lis, i) for i in range(len(lis))]


for i in list(result):
	print(list(i))