# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:13:31 2020

@author: Hp
"""


from pprint import pprint
from numpy import array,zeros,diag,diagflat,dot

def jacobi(A,B,N=25,X=None):
    if X is None:
        X= zeros(len(A[0]))
    D = diag(A)
    R = A-diagflat(D)
    for i in range(N):
        X=(B-dot(R,X))/D
    return X

A = array([[3,-0.1,-0.2],
           [0.1,7,-0.3],
           [0.3,-0.2,10]])
B = array([7.85,-19.3,71.4])

guess = array([1,1,1])
sol = jacobi(A,B,N=25,X=guess)
print("A:")
pprint(A)
print("B:")
pprint(B)
print("X:")
pprint(sol)