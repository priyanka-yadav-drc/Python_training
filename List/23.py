import itertools
original_list = [[2,3],[1,8,5,6], [-9], [7,-9,0]]
new_merged_list = list(itertools.chain(*original_list))
print(new_merged_list)
