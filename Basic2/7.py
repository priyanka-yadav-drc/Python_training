import collections
import pprint

file_input = raw_input('File Name: ')
with open(file_input, 'r') as f:
  count = collections.Counter(f.read().upper())
  value = pprint.pformat(count)
print(value)