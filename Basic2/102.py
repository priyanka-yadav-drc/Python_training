def func(txt):
	result=[]
	result.append(txt[0])
	for i in range(1,len(txt),1):
		if txt[i]!=txt[i-1]:
			result.append(txt[i])

	return ''.join(result)

print(func("PPYYTTHHOOON"))