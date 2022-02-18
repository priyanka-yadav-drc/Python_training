import os
import glob

files=glob.glob("*.py")

files.sort(key=os.path.getmtime)
print(files)