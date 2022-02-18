from functools import reduce
nums = [1,2,3,4]
print("Original list numbers:")
print(nums)
nums_product = reduce( (lambda x, y: x * y), nums)
print("Product of the said numbers :",nums_product)
