# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:40:29 2017

@author: Angies computer
"""

# Fibonacci version recursiva con memoizacion


global contadora3
contadora3 = 0
cache = {0: 0, 1: 1}

def fib(n):
    global contadora3 
    contadora3 = contadora3 +1
    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

x=[]
f=[]
for i in range(1,100):
    x.append(i)
    contadora3=0
    cache = {0: 0, 1: 1}
    fib(i)
    f.append(contadora3)


    