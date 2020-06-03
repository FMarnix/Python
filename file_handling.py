#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 00:12:23 2020

@author: filipeneto
"""

f = open("test.txt", "a")
f.write("\nThis text will overwrite the content of our file")

f = open("test.txt")
print(f.read())