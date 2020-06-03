#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:48:55 2019

@author: filipeneto
"""

# Print a multiplication table to 10 X 10
# Print columm heading
print("      1    2    3    4    5    6    7    8    9    10")
print("  +--------------------------------------------------")
for row in range(1, 11):          # 1 <= row <= 10, stable has 10 rows
    if row < 10:                  # Need to space?
        print(" ", end="")
    print(row, "| ",end="")       # Print heading for this row.
    for column in range (1, 11):  # Table has 10 columms.
        product = row*column;     # Compute product
        if product < 100:         # Need to ad space?
            print(end=" ")        
        if product < 10:          # Need to add another
            print(end=" ")
        print (product, end=" ")  # Display product
    print()                       # Move cursor to next row