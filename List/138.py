mixed_list=['a',4,'l',10,'f']
int_part = sorted([i for i in mixed_list if type(i) is int])
str_part = sorted([i for i in mixed_list if type(i) is str])
print(int_part+str_part)