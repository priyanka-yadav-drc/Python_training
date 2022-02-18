lst=[[1,2,3],[2,4,5],[2,7,8]]
print(lst[0])

temp = set(lst[0]).intersection(*lst)
print(list(temp))
