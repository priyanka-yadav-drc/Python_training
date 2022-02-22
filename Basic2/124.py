def func(txt):
	for i in range(1,len(txt)):
		if txt[i]==txt[i-1]:
			return True
	return False

print(func("PHHP"))
print(func("PHP"))