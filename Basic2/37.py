n=input("enter the number: ")

from itertools import permutations
lis=[x for x in range(10)]
comb=list(permutations(lis,4))
count=0
for x in comb:
	if sum(x)==n:
		count+=1

print("number of combinations={}".format(count))