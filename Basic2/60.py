txt=raw_input("Enter a sentence: ")
print([y for y in txt.split() if 3<=len(y)<=6])