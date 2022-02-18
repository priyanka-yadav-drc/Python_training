str=raw_input("String: ")
n=int(raw_input("num: "))
result=""
if len(str) <2 :
	i=0
	while i<n :
		result=result+str
		i=i+1
else :
	i=0
	res=str[:2]
	while i<n :
		result=result+res
		i=i+1

print(result)