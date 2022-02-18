chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Original lists:")
print(chars)
merge_from = 2
merge_to = 4
result = chars
result[merge_from:merge_to] = [''.join(result[merge_from:merge_to])]
print(result)