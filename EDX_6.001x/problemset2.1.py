#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:47:37 2020

@author: filipeneto
"""

def remaining_balance(balance, annualInterestRate, monthlyPaymentRate):

    paid = 0
    
    for month in range(1,13):
        mir= annualInterestRate/12.0     # mir == Monthly interest rate
        mip = round(MonthlyPaymentRate * balance, 2)    # mip == Minnimun monthly payment
        mub = balance - mip  # mub == Monthly unpaid balance
        ubea = round(mub + (mir * mub), 2) # Updated balance each month
        
        print("Month: ", month)
        print("Minimum monthly payment: ", str(mip))
        print("Remaining balace: ", str(ubea)
        
        balance = ubea
        paid += mip

    