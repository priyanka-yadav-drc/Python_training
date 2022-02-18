from random import shuffle 
lis=["abcd","efgh","ijkl"]

for x in lis :
	x=list(x)
	shuffle(x)
	print(''.join(x))