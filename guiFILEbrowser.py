#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:28:53 2019

@author: filipeneto
"""

from tkinter import Tk

from idlelib.Treewidget import ScrolledCanvas,FileTreeItem, TreeNode
import os

root = Tk()
root.title("File browser")
sc = ScrolledCanvas(root, bg="white", highlightthickness=0, takefocus=1)
sc.frame.pack(expand=1, fill="both", side="left")

item = FileTreeItem(os.getcwd())
node = TreeNode(sc.canvas, None, item)
node.expand()

root.mainloop()
