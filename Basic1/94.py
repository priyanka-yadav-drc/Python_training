S =raw_input("Enter string: ") 
nums = []
print("\nConvert bytes of the string to a list of integers:")
for char in S:
   nums.append(ord(char))
print(nums)
