#!/usr/bin/env python3
# -*- coding: utf-8 -*-0
"""
Created on Tue Nov 12 12:24:08 2019

@author: filipeneto
"""

value = eval(input("Please enter a integer in the range 0...5: "))
if value < 70:
    print("Too small")
elif value == 0:
    print("zero")
elif value == 1:
    print("one")
elif value == 2:
    print("two")
elif value == 3:
    print("three")
elif value == 4:
    print ("four")
elif value == 5:
    print("five")
else:
    print("Too large")
print("Done")
    