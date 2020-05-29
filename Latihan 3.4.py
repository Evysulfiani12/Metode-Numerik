# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:27:09 2020

@author: Hp
"""


def f(x):
    return 3*x**2 - 10

def df(x):
    return 6*x

def newtonRaphson(f, df, x, tol):
    a = f(x)
    iterasi = 0
    while abs(a) > tol and iterasi < 100:
        try:
            x = x - float(a)/df(x)
        except ZeroDivisionError:
            print("Error! - turunan bernilai 0 untuk  x = ", x)

        a = f(x)
        iterasi += 1

    if abs(a) > tol:
        iterasi = -1
    return x, iterasi
root,numlter = newtonRaphson(f, df, x=100, tol=1.0e-6)

if numlter > 0:
    print("Jumlah iterasi : %d" % (1 + 2*numlter))
    print("Akar: %f" % (root))
else:
    print("Solusi tidak ditemukan!")