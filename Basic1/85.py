import os

path="/home/priyanka/"
print(path)
if os.path.isdir(path):
	print("it is a directory")
elif os.path.isfile(path):
	print("it is a file")