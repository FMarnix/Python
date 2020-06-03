#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:39:27 2019

@author: filipeneto
"""

# i, j, and k are numbers

i = 7
j = 5
k = 3

if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
        
print("i =", i, " j =", j, " k =", k)