#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 18:47:53 2020

@author: filipeneto
"""



def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N == 0:
        return 0
    else:
         return (N % 10 == 7) + count7(N // 10)