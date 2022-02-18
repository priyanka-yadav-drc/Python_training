import sys,string

def func(string,alphabet=string.ascii_lowercase):
	alpha=set(alphabet)
	string1=set(string.lower())
	return alpha<=string1

print(func('The quick brown fox jumps over the lazy dog'))