# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:37:51 2020

@author: Hp
"""


import numpy as np

n=int(input('input jumlah pasangan nilai='))
x=np.zeros((n))
y=np.zeros((n))

for k in range(0,n):
    print('input x [{}]='.format(k),end="")
    x[k]=float(input())
    print('input y[{}]='.format(k),end="")
    y[k]=float(input())

X = float(input('input nilai X yang ini dicari pasangannya='))
yp=0

for i in range(n):
    p=1
    for j in range(n):
        if j !=i:
            p*=(X-x[j])/(x[i]-x[j])
    yp+=y[i]*p

print('x=%.2f,y=%f'%(X,yp))