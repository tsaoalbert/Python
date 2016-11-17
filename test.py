#!/usr/bin/env python
"""
define a function "line: which prints a line of "n" symbol "c"
"""

import sys
import getopt
import getopt

def printsegment (sym,n): 
    for i in range (n):
       print sym,

def printline (b,f,n1,n2):
    printsegment (b,n1)
    printsegment (f,n2)
    printsegment (b,n1)
    print 


def main():
	b=":"
	f="W"
	n=12
	printsegment (b,2*n+5)
	print 
	for i in range (n-1):
		printline (b,f, n-i+2, 2*i+1)     
    
	for i in range (n):
		printline (b,f, i+1+2, 2*(n-i)-1)
	printsegment (b,2*n+5)    
	print type(32)



if __name__ == "__main__":
	sys.exit(main())
     
