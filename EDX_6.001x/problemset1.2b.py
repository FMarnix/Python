#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:40:20 2020

@author: filipeneto
"""

s = 'azcbobobegghaklbob'
a = 'bob'
results = 0
sub_len = len(a) 
for i in range(len(s)):
    if s[i:i+sub_len] == a: 
        results += 1

print ("Number of times bob occurs is: ",  results)