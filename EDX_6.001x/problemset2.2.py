#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 23:06:04 2020

@author: filipeneto
"""


balance = 3329
annualInterestRate = 0.2

minnimunPayment = 0
monthlyInterestRate = annualInterestRate/12
unpaidBalance = balance

while balance > 0:
    for i in range(12):
        balance = balance - minnimunPayment + ((balance - minnimunPayment) * monthlyInterestRate)
    if balance > 0:
        minnimunPayment += 10
        balance = unpaidBalance
    elif balance <= 0:
        break
print('Lowest Payment: ', minnimunPayment)