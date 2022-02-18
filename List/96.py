input_list=[[1,5,3,10],[6,4,3],[8,0]]
result = list(map(sorted, input_list))
result.sort(key=len)
print(result)