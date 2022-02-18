lis=["hello how are you","priyanka ravindra yadav "]
result = [a for ls in lis for a in zip(ls.split(" ")[:-1], ls.split(" ")[1:])]
print(result)