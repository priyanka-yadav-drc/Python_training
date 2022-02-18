lst= [1,2,3,4,5,6,7,8,9,0]  
n=3
ele="a"
result = []
for st_idx in range(0, len(lst), n):
        result.extend(lst[st_idx:st_idx+n])
        result.append(ele)
result.pop()  

print(result)