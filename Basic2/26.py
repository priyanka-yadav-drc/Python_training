from itertools import combinations

lis=[1,2,3]

n=list(combinations(lis,2))
print(n)
sum=0
for x in n:
	sum+=abs(x[1]-x[0])

print("sum={}".format(sum))
