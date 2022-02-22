def func(nums):
	p_sum=0
	n_sum=0
	for x in nums:
		if x<0:
			n_sum+=x
		else:
			p_sum+=x

	if abs(n_sum)>p_sum:
		return n_sum
	else:
		return p_sum
print(func([1,-2,3,-4,0]))