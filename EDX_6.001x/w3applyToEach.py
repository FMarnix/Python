#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 00:22:35 2020

@author: filipeneto
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

def applyFuns(L, x):
    for f in L:
        print(f(x))

applyFuns([abs], testList)