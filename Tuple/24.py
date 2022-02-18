lis=[1,2,3,4,(6,),8]
count=0
for x in lis:
	if isinstance(x,tuple):
		break
	count+=1
print(count)