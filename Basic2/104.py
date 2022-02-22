def lucky_Numbers(matrix):
    result = set(map(min, matrix)) & set(map(max, zip(*matrix)))
    return list(result)


m1 = [[1,2,3], [3,4,5]]
print "\nOriginal matrix:",m1
print "Lucky number(s) in the said matrix: ",lucky_Numbers(m1)


