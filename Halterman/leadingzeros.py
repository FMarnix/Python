#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 00:27:17 2019

@author: filipeneto
"""

# Request input from the user
num = eval(input("Please enter an integer in the range 0...9999: "))

#Attenuate the number if necessary
if num < 0:        #Make sure number is not to small
    num = 0
if num > 9999:     #Make sure number is not too big
    num = 9999
    
print(end="[")  #pRINT LEFT BRACE
    
#EXtract and print thousands-place digit
digit = num/1000     # Determines the thousands-place digit
print(digit, end="")  # Print the thousands-place digit
num %= 1000          # Discard thousands-place digit

#Extract and print hundreds-place digit
digit = num/100       # Determines the hundreds-place digit
print(digit, end="")  # Print the hundreds-place digit
num %= 100            # Discad hundreds-places digit
    
#Extract and print tens-place digit
digit = num//10      # Determines the tens-place digit
print(digit, end="") # Print the tens-place digit
num %= 10            # Discard tens-place digit
    
# Remainder is the one-place digit
print(num, end="")  #Print the ones-place digit
    
print("]")
    
