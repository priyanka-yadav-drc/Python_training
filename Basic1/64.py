import os.path, time
print "Last modified: " , time.ctime(os.path.getmtime("test.txt"))
print "Created: " , time.ctime(os.path.getctime("test.txt"))
