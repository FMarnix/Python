#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:40:13 2019

@author: filipeneto
"""

sum = 0
done = False;
while not done:
    val = eval(input("Enter positive integer(999 quits):"))
    if val < 0:
        print("Negative value", val, "ignored")
        continue;  # Skip rest of the body for this iteration
    if val != 999:
         print("Tallying", val)
         sum += val
    else:
         done = (val == 999);   # 999 entry exits loop
 

print("sum =", sum)
