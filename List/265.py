n=input("enter n: ")
i=2
f=[0,1]

while i<n:
	x=f[(i-2)]+f[(i-1)]
	f.append(x)
	i+=1
print(f)
