#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:48:47 2019

@author: filipeneto
"""

val = eval(input(28))
if val < 10:
    if val != 5:
        print("wow", end='')
    else:
        val +=1
else:
    if val == 17:
        val += 10
    else:
        print("whoa ", end='')
        
print(val)