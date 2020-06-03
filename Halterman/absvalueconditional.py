#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 12:31:03 2019

@author: filipeneto
"""

#acquire a number from the user and print its abslute number.
n = eval(input("Enter a number "))
print('I', n, 'I = ', (-n if n < 0 else n), sep='')