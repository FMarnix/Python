#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 00:16:58 2020

@author: filipeneto
"""

s = 'azcboboegghakl'

string =""             #taking a plain string to represent the then generated string
present =""             #the present/current longest string
for i in range(len(s)): #not len(s)-1 because that totally skips last value
    j = i+1            
    if j>= len(s):    
        j=i           #using s[i+1] simply throws an error of not having index
    if s[i] <= s[j]:  #comparing the now and next value
        string += s[i] #concatinating string if above condition is satisied
    elif len(string) != 0 and s[i] > s[j]: #don't want to lose the last value
        string += s[i] #now since s[i] > s[j] #last one will be printed
        if len(string) > len(present): #1 > 0 so from there we get to store many values
            present = string #swapping to largest string
        string = ""
    if len(string) > len(present): #to swap from if statement
        present = string
if present == s[len(s)-1]: #if no alphabet is in order then first one is to be the output
    present = s[0]
print('Longest substring in alphabetical order is:' + present)