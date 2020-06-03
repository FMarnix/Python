#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:44:12 2019

@author: filipeneto
"""

print("Help! My Computer doesn't work!")
while True:
    print("Does the computer make any sounds(fans,etc.)")
    choice = input("or show any lights? (y/n):")
    # The troubleshooting control logic
    if choice == 'n':  # The computer does not have powery
        if choice == 'n': # It is not plugged in, plug it in
            print("Plug it in.")
        else:   # It is plugged in
            choice = input("Is the switch in the \"on\" position? (y/n):")
            if choice == 'n': # The switch is off, turn it on!
                print("Turn it on.")
            else:   # The switch is on
                choice = input("Does the computer have a fuse? (y/n):")
                if choice == 'n': # No fuse
                    choice = input("Is the outlet OK? (y/n):")
                    if choice == 'n': # Fix outlet
                        print("Check th outlet's circuit ")
                        print("braker or fuse. Move to a")
                        print("new outlet, if necessary. ")
                    else:   #Beats me!
                        print("Please consult a service technician.")
                        break   # Nothing else i can do, exit loop
                else:  # Check fuse
                        print("Check the fuse. Replace if ")
                        print("necessary.")
    else:    # The computer has power
        print("Please consult a service technician.")
        break   # Nothing else i can do, exit loop
        
        
            