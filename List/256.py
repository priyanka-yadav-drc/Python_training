from itertools import chain,combinations
li=[1,2,3]
print(list(chain.from_iterable(combinations(li,r) for r in range(len(li)+1))))