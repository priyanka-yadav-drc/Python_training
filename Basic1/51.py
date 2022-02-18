import cProfile
def func():
    print("name= priyanka")
    x=1
    y=2
    print(x+y)
cProfile.run('func()')