#!/usr/bin/python
import math

from multiprocessing import Pool
def f(x):
    while True:
        math.factorial(x)
        
if __name__ == '__main__':
    
    processes = 8 
    pool = Pool(processes = processes)
    large_num=10000
    result = pool.map(f, range(large_num,large_num+8))
    pool.close()
    pool.terminate()
