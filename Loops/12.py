lines = []
while True:
    l = raw_input()
    if l:
        lines.append(l.lower())
    else:
        break;

for l in lines:
    print(l)
	