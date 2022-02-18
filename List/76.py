from itertools import groupby
def func(alist):
        def ctr_ele(el):
            if len(el)>1: return [len(el), el[0]]
            else: return el[0]
        return [ctr_ele(list(group)) for key, group in groupby(alist)]

n_list = [1,1,2,3,4,4,5, 1]
print("Original list:") 
print(n_list)
print("\nList reflecting the modified run-length encoding from the said list:")
print(func(n_list))


