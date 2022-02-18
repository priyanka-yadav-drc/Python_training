from itertools import izip_longest as zip_longest
nums = [[0, 1, 2],
       [2, 3, 4],
       [3, 4, 5, 6],
       [7, 8, 9, 10, 11],
       [12, 13, 14]]

def get_avg(x):
    x = [i for i in x if i is not None]
    return sum(x, 0.0) / len(x)
result = map(get_avg, zip_longest(*nums))

print(list(result))
