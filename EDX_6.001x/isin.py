#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:19:19 2020

@author: filipeneto
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is un aStr; False otherwise
    '''
    # Your code here
    if aStr == "":
        return False
    elif len(aStr) == 1 and aStr == char:
        return True
    elif len(aStr) == 1 and aStr != char:
        return False
    elif aStr[len(aStr)//2] == char:
        return True
    else:
        if char < aStr[len(aStr)//2]:
            return isIn(char, aStr[:len(aStr)//2])
        else:
            return isIn(char, aStr[len(aStr)//2:])