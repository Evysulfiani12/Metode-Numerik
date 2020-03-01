# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:33:05 2020

@author: User
"""

import math
def f(x):
    return x**3-10*x**2+5

a = 0.7
b = 0.9
e = 0.0000001
N = 100
iterasi = 0

print("===============================")
print("    c               c(c)")
print("===============================")
while True:
    iterasi +=1
    c = (b-f(b)*(b-a)/(f(b)-f(a)))
    if f(a)*f(c)<0:
        b=c
    else:
        a=c
    print("{:7.5f} \t {:+15.10}".format(c,f(c)))
    if abs(f(c)) <= e or iterasi >= N:
        break
print("++++++++++++++++++++++++++++++++")
