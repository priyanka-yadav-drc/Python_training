print("Input the values of a,b,c,d,e,f: ")
int_num = list(map(int,raw_input().split()))
a,b,c,d,e,f=int_num

n = a*e - b*d
print("Values of x and y:")
if n != 0:
    x = (c*e - b*f) / n
    y = (a*f - c*d) / n
    print('{:.3f} {:.3f}'.format(x+0, y+0))
