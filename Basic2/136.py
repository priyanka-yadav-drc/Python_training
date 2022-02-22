def func(txt):
	return ' '.join([i[::-1] if len(i)%2==1 else i for i in txt.split()])

print(func("hello how are your parents"))