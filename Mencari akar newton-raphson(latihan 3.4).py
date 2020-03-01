# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 01:18:24 2020

@author: User
"""
#metode neowton untuk mencari akar
#fungsi fx=x^2-16

import math
iterasi= 70
x=8    #nilai tebakan
fx=x**2 - 16
batas=0.01
i=0

while (i<=iterasi and abs (fx)>batas):
    fx=x**2 - 16
    ft=2**4 + 2
    x=x-(fx/ft)
    print ('x =',x,      'fx = ',fx)
    i=i+1
print ('akarnya adalah',x,'dengan iterasi sebanyak',i,'kali')