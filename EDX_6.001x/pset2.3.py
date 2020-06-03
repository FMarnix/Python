#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:21:08 2020

@author: filipeneto
"""

balance = 4123
annualInterestRate =0.18
lowerBound = balance/12
upperBound = (balance * (1 + annualInterestRate / 12)**12) / 12
fixedMonthlyPayment = round((lowerBound + upperBound) /2, 2)

while True:
    # loop over each month of a year
    for i in range(12):
        remainingBalance = balance - fixedMonthlyPayment
        balance = round((remainingBalance + remainingBalance * annualInterestRate /12), 2)
    # if the balance is near zero, print out value of fixedMonthlyPayment, break the loop
    if(abs(balance - 0)) < 0.1:
        print("Lowest Payment: " + str(round((fixedMonthlyPayment), 2)))
        break
    else:
        # iff balance is less than zero, means fixedMonthlyPayment is too high
        if balance < 0:
            upperBound = fixedMonthlyPayment
        # if balance is more than zero, means fixedMonthlyPayment is too low
        elif balance > 0:
            lowerBound = fixedMonthlyPayment
        # try new fiedMonthlyPayment
        fixedMonthlyPayment = (lowerBound + upperBound) / 2
    