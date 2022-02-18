nums=[8,2,4,3,1,9,0,6,5,7]
lr=3
hr=6
temp = []
for idx, el in enumerate(nums):
        if idx >= lr and idx < hr:
            temp.append(el)
result_max = max(temp)     
result_min = min(temp)
print(result_max)
print(result_min)