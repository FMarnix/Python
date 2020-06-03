#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 12:53:43 2019

@author: filipeneto
"""

#File computesquareroot

# Get the value from the user
val = eval(input('Enter a number: '))
# Compute a proisional square root
root = 1.0;

# How far off is our provisional root?
diff = root*root - val

# Loop until the provisional root
# is close enough to the actual root
while diff > 0.00000001 or diff< -0.00000001:
    root = (root + val/root) / 2
    print(root, 'squared is', root*root)
    # How bad is our current approximation?
    diff = root*root - val
    
# Report approximate square root 
    print('Square root of', val , "=", root)