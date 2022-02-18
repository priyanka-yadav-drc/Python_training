n=input("enter total numbers n= ")
s=input("enter step: ")
a=input("enter start number: ")
i=0
result=[a,]
while i<n-1:
	result.append(result[i]+s)
	i+=1

print(result)