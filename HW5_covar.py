
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy.stats
from scipy.stats import poisson
from numpy import *
import numpy as N
import pylab as P
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

"""
omework 5
1.  Navigate to the Fama-French data web site and download the weekly return series 
for the risk free rate, the excess stock return, SMB and HML for the past 50 years. 
Use this data to compute the following results:
(a)  Compute the covariance matrix of returns for each of the 
five 10-year blocks of data.
Do you see a trend in the variances? How about the covariances?  
(b)  What is the empirical relation between the variance values in each 10-year block 
and the covariances?  


"""

def HW5Q1():
    x1 = [-2.1, -1,  4.3]  # first 10 year of returns, to be replaced with the real data    
    x2 = [3,  1.1,  0.12]   # 2nd 10 year of returns
    x3 = [-2.1, -1,  4.3]  # 3rd 10 year of returns
    x4 = [3,  1.1,  0.12]  # 4th 10 year of returns
    x5 = [3,  1.1,  0.12]  # 5th 10 year of returns
    n = len ( x1 )

    X = np.vstack((x1,x2,x3,x4,x5))
    #print X
    Y= np.cov (X)

    n = Y[0].size 
    for i in range ( n ):
        for j in range (n  ):
            y = Y [ i ] [ j ] 
            print "%10.2f   " % y,
        print 



"""
2. Using the WRDS data web site, download the returns on a bond index and 
a stock index of your choosing. Do so for the past 50 years (daily).

(a) Compute the mean and standard deviation of returns of the two indexes.

(b) Suppose you invested $1 in each index 50 years ago and every day re-invested the returns. 

Plot the value of the $1 in each index over the 50-year period. 
How much does each $1 become after 50 years?

(c) Now suppose you were clairvoyant, and knew in advance which index would perform better each day, 
and invested all your cumu- lated money each day in the better index. 
How much would your $1 be worth after 50 years? Compare your answer to the ones in the previous part and comment.

"""

def finalReturns ( Idx , name ):
    mu = np.mean ( Idx );
    std = np.std ( Idx );

    print mu
    print std
    ans = 1;
    n = len ( Idx );
    for i in range ( n):
        ans *= (1+Idx [i])
    print  name, " index in 50 years ==> ", ans
    
def HW5Q2():
    # monthly  bound index, to be replaced with the real data of daily return   
    boundIdx = [.00852, .01045,.00573, .01578, -.01223, .00682, .00452    ]
    stockIdx = [.00852, .01045,.00573, .01578, -.01223, .00682, .00452 ]    #  stock index

    better = [] ;


    for i in range ( len (boundIdx) ):
        x = boundIdx[i];
        if (boundIdx[i] <  stockIdx[i] ) : 
            x = stockIdx[i]
        better.append (x)
    
    print better
    finalReturns ( boundIdx, "Bound" ); 
    finalReturns ( stockIdx  , "Stock" );
    finalReturns ( better   , "The better" );


HW5Q1()

HW5Q2()
