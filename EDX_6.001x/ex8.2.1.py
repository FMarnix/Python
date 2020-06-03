#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 23:41:36 2020

@author: filipeneto
"""

def fancy_divide(numbers, index):
#    try:
#        denom = numbers[index]
#        for i in range(len(numbers)):
#            numbers[i] /= denom
#    except IndexError:
#        print("-1")
#    else:
#        print("1")
#    finally:
#        print("0")
        
        
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")
        
#    try:
#        try:
#            denom = numbers[index]
#            for i in range(len(numbers)):
#                numbers[i] /= denom
#        except IndexError:
#            fancy_divide(numbers, len(numbers) - 1)
#        else:
#            print("1")
#        finally:
#            print("0")
#    except ZeroDivisionError:
#        print("-2")