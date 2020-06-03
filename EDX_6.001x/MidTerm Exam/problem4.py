#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 18:47:53 2020

@author: filipeneto
"""


L = [[1, 2], [3, 4], [5, 6, 7]]


def deep_reverse(L):
    reverse = []
    for i in L:
        reverse.append(i[::-1])
    L[:] = reverse[::-1]
    return L