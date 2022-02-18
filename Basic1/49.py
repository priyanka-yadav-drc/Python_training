from os import listdir
from os.path import isfile, join

files_list = [f for f in listdir('/home/priyanka/Python_Programs/Basic1') if isfile(join('/home/priyanka/Python_Programs/Basic1', f))]
print(files_list);
