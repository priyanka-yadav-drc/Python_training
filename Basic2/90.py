def func(txt):
	l=len(txt)
	txt=list(txt)
	i='*'
	for x in range(l-5):
		txt[x]=i

	return (''.join(txt))

print(func('abcde12345'))