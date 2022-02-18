x = [(4, 1), (1, 2), (6, 0),(5,0),(7,5)]
print(min(x, key=lambda n: (n[1], -n[0])))
