#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 12:28:55 2019

@author: filipeneto
"""

import shutil
import os
import time
import subprocess

def Read():
    path=input("Enter the file path to read:")
    file=open(path, "r")
    print(file.read())
    input('Press Enter...')
    file.close()
    
def Write():
    path=input("Enter the path of file to write or create:")
    if os.path.isfile(path):
        print('Rebuilding the existing file')
    else:
        print('Creating a new file')
    text=input("Enter text:")
    file=open(path,"w")
    file.write(text)
    
def Add():
    path=input("Enter the file path:")
    text=input("Enter the text to add:")
    file=open(path,"a")
    file.write('\n'+text)
    
def Delete():
    path=input("Enter the path of file for deletion:")
    if os.path.exists(path):
        print('File Found')
        os.remove(path)
        print('File has been deleted')
    else:
        print('File Does not exist')
        
def Dirlist():
    path=input("Enter the Directory path to display:")
    sortlist=sorted(os.listdir(path))
    i=0
    while(i<len(sortlist)):
        print(sortlist[i]+\n')
        i+=1
        
def Check():
    fp=int(input('Check existence of \n1.File \n2.Directory\n'))
    if fp==1:
        path=input("Enter th file path:")
        os.path.isfile(path)
        if os.path.isfile(path)==True:
            print('File Found')
        else:
            print('File not found')
    if fp==2:
        path=input("Enter the directory path:")
        os.path.isdir(path)
        if os.path.isdir(path)==False:
            print('Directory Found')
        else:
            print('Directory Not Found')

def Move():
    path1=input('Enter the source path o file to move:')
    mr=int(input('1.Rename \n2.Move \n'))
    if mr==1:
        path2=input('Enter the destination path and file name:')
        shutil.move(path1,path2)
        print('File renamed')
    if mr==2:
        path2=input('Enter the path to move:')
        shutil.move(path1,path2)
        print('File moved')

def Copy():
    path1=input('Enter the path of the file to copy or rename:')
    path2=input('Enter the path to copy to:')
    shutil.copy(path1,path2)
    print('File copied')
    
def Mkdir():
    path=input("Enter the directory name with to make \neg. C:\\Hello\\Newdir \ nWhere Newdir is new directory:")
    os.makedirs(path)
    print('Directory Created')
    