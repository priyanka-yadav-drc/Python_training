lst=[7,2,3,4,5,6,1]
x = lst.pop(0)
y = lst.pop()
lst.insert(0, y)
lst.insert(len(lst), x)
print(lst)