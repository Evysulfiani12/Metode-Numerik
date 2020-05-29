# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:28:53 2020

@author: Hp
"""


import math 
def f(x): 
    return x**3 + 2*x**2 + 10*x - 20
a = 1
b = 1.5
e = 0.000001 
N = 100
iterasi = 0

print('==================================')
print(' c                   f(c)')
print('==================================')

while True: 
    iterasi += 1 
    c = (a + b)/2 
    if f(a)*f(c) < 0: 
        b = c 
    else: 
        a = c
    print('{:7.6f} \t {:+15.10f}'.format(c, f(c))) 
    if abs(f(c)) < e or iterasi >= N:
        break
print('==================================')