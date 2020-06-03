#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 00:25:14 2020

@author: filipeneto
"""

low = 0
high= 100
print("Please think of a number between 0 and 100!")
while True:
    guess = (high + low)//2
    print("Is your secret number ", str(guess), "?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate i guessed correctly. ")
    if answer == 'c':
        print("Game over. Your secret number was: ", str(guess))
        break
    elif answer == 'l':
        low = int(guess)
    elif answer == 'h':
        high = int(guess)
    else:
        print("Sorry, I did not understand your input.")   
