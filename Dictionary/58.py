from itertools import combinations
students = {'V' : [1, 4, 6, 10], 'VI' : [1, 4, 12], 'VII' : [1, 3, 8]} 

result=list(map(dict, combinations(students.items(),2)))
print(result)
