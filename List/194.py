nums = [[1,2,4],[2,4,4],[1,2]]

result =  [sum(x) for x in zip(*map(lambda x:x+[0]*max(map(len, nums)) if len(x)<max(map(len, nums)) else x, nums))]
print(result)