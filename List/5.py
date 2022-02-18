lis=['aba','ab','bbb','fgj']

count=0

for x in lis:
	if len(x)==2:
		count+=1
	elif x[0]==x[-1]:
		count+=1

print(count)