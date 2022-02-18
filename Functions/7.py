def func(str):
	low=0
	up=0
	for s in str:
		if s.islower():
			low+=1
		elif s.isupper():
			up+=1

	print("no of lower case: {}".format(low))
	print("no of upper case: {}".format(up))

func('Hello WorlD')