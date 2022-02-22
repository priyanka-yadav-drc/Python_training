def func(txt):
	nums=list(map(int,txt.split()))

	return max(nums),min(nums)

print(func('3 2 66 89'))