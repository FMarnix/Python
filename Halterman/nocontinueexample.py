#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:00:10 2019

@author: filipeneto
"""

sum = 0
done = False;
while not done:
    val = eval(input("Enter positive integer (999 quits):"))
    if val < 0:
        print("Negative value", val, "ignored")
        continue;  # Skip the rest of body for this iteration
    if val != 999:
        print("Tallying", val)
        sum += val
    else:
        done = (val == 999);   # Entry exits loop
        
print("sum =", sum)