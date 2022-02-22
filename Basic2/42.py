print("Input 6 numbers:")
lis =[x for x in map(float, raw_input().split())] 
print(lis)
lis.sort(reverse=True)
print("sorted list: {}".format(lis))