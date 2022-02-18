l=1
r=10
list1 = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
result=[x for x in list1 if  min(x)>=l and max(x)<=r]
print(result)