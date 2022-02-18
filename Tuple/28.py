tuple_str =  (('333', '33'), ('1416', '55'))
print(tuple_str)
result= tuple((int(x[0]),int(x[1])) for x in tuple_str)
print(result)