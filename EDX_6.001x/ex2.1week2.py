#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:25:05 2020

@author: filipeneto
"""

x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2 - x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break
        
if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))