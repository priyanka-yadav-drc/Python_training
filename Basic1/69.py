x=int(raw_input("Enter num: "))
y=int(raw_input("Enter num: "))
z=int(raw_input("Enter num: "))

x1=min(x,y,z)
y1=max(x,y,z)
z1=(x+y+z)-x1-y1

print(x1,z1,y1)