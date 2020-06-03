#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:21:46 2019

@author: filipeneto
"""

# Print  MAX x MAX  multiplication table
MAX = 18

# First, print heading
print(end="    ")
# Print columm heading numbers
for columm in range(1, MAX + 1):
    print(end=" %2i " % columm)
print()   # Go down to the next line

# Print line separator; a portion for each columm
print(end="   +")
for columm in range(1, MAX + 1):
    print(end="----") # Print the portion of line
print()    # Go down to the next line

# Print tabale contents
for row in range(1, MAX + 1):
    print(end="%2i | " % row)
    for columm in range(1, MAX + 1):
        product = row*columm;
        print(end="%3i " % product)
    print()
 