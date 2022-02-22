def func(txt):
	m=len(txt)//2
	if len(txt)%2!=0:
		return txt[m]
	else:
		return ''.join([txt[m-1],txt[m]])

print(func("hello"))
print(func("priyanka"))