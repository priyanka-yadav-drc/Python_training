n=input("enter how many numbers choosen: ")
z=input("enter sum: ")
from itertools import combinations
lis=[x for x in range(10)]
comb=list(combinations(lis,n))
count=0
for x in comb:
	if sum(x)==z:
		count+=1

print("number of combinations={}".format(count))