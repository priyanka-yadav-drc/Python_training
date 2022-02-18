tup=(1,2,3,4)
n=(5,)
print(tup+n)
tup=tup[:2]+n+tup[2:]
print(tup)