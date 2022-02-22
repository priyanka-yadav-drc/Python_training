txt=raw_input("Enter string:")
nums=['0','1','2','3','4','5','6','7','8','9']
sum=0
for x in txt:
	if x in nums:
		sum+=int(x)

print(sum)
