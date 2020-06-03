#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:34:38 2020

@author: filipeneto
"""

vowels = 0
s = input('Enter your string: ')
for i in s:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' 
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
        
print('Number of vowels: ' + str(vowels))
    