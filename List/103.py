from itertools import groupby

lis=[2,2,2,1,5,7,8,8,8]
n=3
result=[i for i,j in groupby(lis) if len(list(j))==n]
print(result)