import random
def func(filename):
    lines = open(filename).read().splitlines()
    return random.choice(lines)
print(func('demo.txt'))
