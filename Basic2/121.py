def func(txt):
	lis=list(txt)

	for i in range(len(lis)):
		if lis[i]=='P':
			lis[i]=9
		elif lis[i]=='T':
			lis[i]=0
		elif lis[i]=='S':
			lis[i]=1
		elif lis[i]=='H':
			lis[i]=6
		elif lis[i]=='A':
			lis[i]=8

	return ''.join(''.join(str(lis)))

print(func("PHP"))
print(func("PRIYANKA"))
print(func("THESE"))