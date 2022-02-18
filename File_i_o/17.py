f=open("demo.txt").readlines()
result=[s.rstrip('\n') for s in f]
print(result)