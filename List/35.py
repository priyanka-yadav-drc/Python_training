lis=['a','b']
n=5
new_lis=["{}{}".format(x,y) for y in range(1,n+1) for x in lis]
print(new_lis)