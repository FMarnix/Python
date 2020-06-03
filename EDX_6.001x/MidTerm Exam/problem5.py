#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:25:21 2020

@author: filipeneto
"""

def keysWithValue(aDict, target):
    newList = []
    if target not in aDict.values():
        return newList
    else:
        for i in aDict.keys():
            if target == aDict[i]:
                newList.append(i)
                newList.sort()
    return newList