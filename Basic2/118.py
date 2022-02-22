from multiprocessing import Process
import os
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
def f(name):
    info('function f')
    print('hello', name)
if __name__ == '__main__':
    info('Main line')
    p = Process(target=f, args=('priyanka',))
    p.start()
    p.join()
