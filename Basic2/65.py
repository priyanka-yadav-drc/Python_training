def func(txt,sub):
	max_sub=sub[0]
	for x in sub:
		if len(x)>len(max_sub):
			max_sub=x
	return max_sub





print(func("pythonexercises", ["py", "ex", "exercises"]))