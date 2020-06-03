#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:39:27 2020

@author: filipeneto
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    balance = balance - (balance * monthlyPaymentRate) + \
    ((balance - (balance * monthlyPaymentRate)) * (annualInterestRate/12))
print("Remaining balance:", round(balance, 2))