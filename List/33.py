from itertools import combinations

lis=['7','2','9','8']
n=len(lis)
i=1

while i<=n:
	a=combinations(lis,i)
	y=[''.join(x) for x in a]
	print(y)
	i=i+1

