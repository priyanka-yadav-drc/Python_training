def func(txt):
	lis=list(txt)
	for i in range(len(txt)):
		if txt[i].islower():
			lis[i]=txt[i].upper()
		elif txt[i].isupper():
			lis[i]=txt[i].lower()
	lis[0]=txt[0].upper()
	return ''.join(lis)

print(func("PrIyanKA"))