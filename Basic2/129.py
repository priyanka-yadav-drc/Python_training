def func(txt):
	result=[]
	for i in range(len(txt)):
		if txt[i].islower():
			result.append(i)
	return result

print(func("HeeLo"))
