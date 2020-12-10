#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:01:52 2019

@author: filipeneto
"""

#Allow the user enter a sequence non profit
# numbers . the user ends the list with a negative
# number at the end the sum of the non negative
# nmvere entered os displayed the program prints
# zero if the user provides no negative numbers

entry = 0
sum = 0

#Request input from the user
print("Enter numbers to sum, negative number ends list:")

while True:                    #Loop forever
    entry = eval(input())      #Get the value
    if entry < 0:              #Is number negative number?
        break                  #If so, exit the loop
    sum += entry               #Add entry ti running sum

print("Sum =", sum)
