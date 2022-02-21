result=[]
nums=[x for x in raw_input().split(',')]
for p in nums:
	x=int(p,2)
	if(x%5==0):
		result.append(p)

print(result)