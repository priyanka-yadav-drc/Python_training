from collections import defaultdict
lis=['a', 'b', 'f', 'a', 'c', 'e', 'a', 'a', 'b', 'e', 'f']
freq=defaultdict(int)
for x in lis:
	freq[x]+=1

print(dict(freq))