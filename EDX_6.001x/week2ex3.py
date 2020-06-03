#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:05:10 2020

@author: filipeneto
"""
L = ['inc', 'square', 'halve', 'abs']
x = -3

L = []

def applyToEach(L, x):
    result =[]
    for i in range(len(L)):
        result.append(L[i](x))
    return result

