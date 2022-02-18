import string

with open("demo.txt","w") as f:
	alphabet = string.ascii_uppercase
	letters = [alphabet[i:i + 2] + "\n" for i in range(0, len(alphabet), 2)]
	f.writelines(letters)
