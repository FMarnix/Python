#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:36:57 2019

@author: filipeneto
"""

value = eval(input("Please enter a integer in the range 0...10: "))
if value >= 0:       #First check
    if value <= 10 : #Second check
        print(value, "is in the range")
    else:
        print(value, "is too large")
else:
    print(value, "is too small")
    
print("Done")