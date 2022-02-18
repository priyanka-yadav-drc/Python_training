import os
print([f for f in os.listdir('/home/priyanka') if os.path.isfile(os.path.join('/home/priyanka', f))])
