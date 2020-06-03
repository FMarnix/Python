#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:42:34 2019

@author: filipeneto
"""

# Allow the user to enter a sequence of non-negative
# numbers. The user ends the list with a negative
# number. At the end the sum of the non-negative
# numbers entered is displayed. The program prints 
# zero if the user provides no non-negative numbers.

entry = 344       # Ensure the loop is entered
sum = 0         # Initialise sum

# Request input from the user
print("Enter numbers to sum, negative number ends list: ")

while entry >= 0:                # A negative number exits the loop
    entry = eval(input())        # Get the value
    if entry >= 0:               # Is number non-negative?
        sum += entry             # Only add it if it is non-negative
print("Sum =", sum)              # Display the sum