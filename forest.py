#!/usr/bin/env python
"""
define a function "line: which prints a line of "n" symbol "c"
"""

import sys
import getopt
"""
"""
import random

def segment(n,c):
    s=""
    for i in range(n):
        s = s + c
    return s

def triangle(m,n,b,c):
    list = []
    for i in range (n/3,n):
        c = (chr) ( ord('0') + i ) 
        s = segment(m-i,b)
        s = s+ segment(2*i+1,c)
        s = s+ segment(m-i,b)
        list.append(s)
    return list

def rectangle(m,w,h,b, c):
    list = []
    bg = segment(m,b)
    for i in range(h):
        s = bg+segment(w,c) + bg
        list.append(s)
    return list

def treeTrunk(m,n,b,c):
    w = n/4;
    h= max(2,w*3);
    return rectangle (m-w,2*w+1,h,b,c)
    
def tree(n,b,c):
    m = n
    list = []
    for i in range (n):
        list = list + triangle(m,i,b,c)

    list =list + treeTrunk(m,n,b,c)
    return list

"""
    Add blank lines on top of each tree so that all tree will be rooted
    at the same ground level
"""
def addBlankLine(list,h,b):
    w = len(list[0])
    s = segment(w,b)
    pre = []
    for i in range(h-len(list)):
        pre.append(s)
    return pre+list

    
def forest(c, hlist):
    xlist = []
    h = 0
    b = "."
    for i in hlist:
        list = tree(i,b,c)
        h = max (h, len(list))
        xlist.append(list)
    ylist = []

    for list in xlist:
        ylist.append( addBlankLine(list,h,b) )
    return ylist
        
        
def printTrees(hlist, c):
    xlist = forest(c, hlist)
    h = len(xlist[0])
    for i in range( h ):
        for list in xlist:
            print list[i],
        print 


def goTest(n):
    c = "*"
    hlist = []
    for i in range(n):
        hlist.append( random.randint(3,10) )
    printTrees(hlist, c)

goTest(5)
        
