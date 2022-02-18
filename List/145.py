nums = [10,20,4,5,'b',70,'a']
print(nums)
print(sum(int(el) for n in nums for el in str(n) if el.isdigit()))