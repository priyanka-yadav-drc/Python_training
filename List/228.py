from math import floor
l1=[2.1, 1.2] 
l2=[2.3, 3.4]

l1=list(map(floor, l1))
l2=list(map(floor, l2))
print(l1)
print(l2)
print(set(l1).difference(set(l2)))