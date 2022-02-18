from itertools import groupby
def compress(l_nums):
	return [key for key, group in groupby(l_nums)]
n=[2,2,2,4,4,5,5,5,6,6,6,2,2]
print(compress(n))