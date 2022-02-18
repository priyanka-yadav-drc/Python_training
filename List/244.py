lis=[]
start=input("Enter start number: ")
end=input("Enter end number: ")
step=input("Enter step: ")

for i in range(start,end+1,step):
	lis.append(i)

print(lis)