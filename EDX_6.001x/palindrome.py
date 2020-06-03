#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:17:20 2020

@author: filipeneto
"""

ans = 0

def isPalindrome(s):
    """
    Assumes s is a str
    Returns True if s is a palindrome; False otherwise.
    Punctuation marks, blanks, and capitalization are
    ignored.
    """
    
    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    
    def isPal(s):
        print('  isPal called with ',s)
        if len(s) <= 1:
            print('  About to return True from base case')
            return True
        else:
            ans = s[0] == s[-1] and isPal(s[1:-1])
            print('   About to return', ans, 'for', s)
            return ans
        
    return isPal(toChars(s))

def testIsPalindrome():
    print('Try dogGod')
    print(isPalindrome('dogGod'))
    print('Try doGood')
    print(isPalindrome('doGood'))
    