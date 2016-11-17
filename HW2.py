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
Homework 2

1. Let X be a normal random variable with a mean of 100 and a standard deviation of 50.
Let Z be a standard normal random variable. Note that X−100/50 has a Z distribution.
(Recall that any normal random variable minus its mean divided by its standard deviation has 
a standard normal distribution.) Use R to help determine
Q1(a) P(Z < 1.78) =  0.962462019651
Q1(b) P( Z > - 0.54) =  0.705401483784
Q1(c) P( X > 80) =  0.65542174161
Q1(d) P( 65<X < 83) =  0.124964611741 

"""

def Q1():
	x = scipy.stats.norm(0, 1).cdf( 1.78)
	print "Q1(a) P(Z < 1.78) = ", x

	x =  1- scipy.stats.norm(0, 1).cdf(- 0.54)
	print "Q1(b) P( Z > - 0.54) = ", x

	x =  1- scipy.stats.norm(100, 50).cdf(80)
	print "Q1(c) P( X > 80) = ", x

	x =   scipy.stats.norm(100, 50).cdf(83) - scipy.stats.norm(100, 50).cdf( 65 )
	print "Q1(d) P( 65<X < 83) = ", x


"""
2. Recall in classthatwesaidifP(X=1)=pandP(X=0)=q=1−p then X’s mean and standard deviation are p and √pq 
respectively. Use the discrete formulas defining the mean and variance from class 
to prove that p and √pq are correct.

==>
see http://www.math.ubc.ca/~feldman/m302/binomial.pdf 
"""


"""
3. Assume each day that the stock of “Cocktail Monkeys and Umbrellas, Inc.” has a 
70% chance of increasing 0.5% (note that’s half a percent, not 50 percent!) and a 
30% chance of decreasing 0.6%. 

Assuming the movement on any given day has no influence upon the movement on any other day, 
determine the probability that after the next 252 trading days the stock will have neither lost more than 
a third of its original value nor gained over a half of its original value. 

Approximate this using the central limit theorem and then compare 
this approximation to the exact value, which you should use R to determine.

==> 
Q3: The approximate probability for price change between 2/3 and 1.5 is  1.0
Q3: The exact probability for price change between 2/3 and 1.5 is  0.393717819167
"""


from scipy.misc import factorial as fact
from scipy.misc import comb

def Q3():
	n = 252 ; #days 
	p = 0.7 ; # prob for rise
	q = 1-p
	priceUp = 1.005
	priceDown = 0.994 
	u = p*priceUp + q*priceDown
	v = p*(priceUp-u)*(priceUp-u) + q* (priceDown-u)*(priceDown-u)
	s = math.sqrt ( v ) 
	x = scipy.stats.norm(u, s).cdf( 1.5 )
	y = scipy.stats.norm(u, s).cdf( 0.6666 ) 
	appro = x-y;
	
	exact = 0 ;
	for i in range(0,n+1): # i = #rise days ==>  n-i == #fall days
		priceChange = math.pow(priceUp, i) * math.pow(priceDown, n-i) #total priceChange over n days
		if (priceChange >= 2.0/3 and priceChange <= 1.5 ):
			exact = exact + comb(n, i, True) * math.pow(p,i) * math.pow(q,n-i) 

	print "Q3: The approximate probability for price change between 2/3 and 1.5 is ", appro
	print "Q3: The exact probability for price change between 2/3 and 1.5 is ", exact



"""
4. Recall that if the random variable X represents the number of times a class of i.i.d. events 
    occur within a fixed time period, then X will have a Poisson distribution. For Poisson distributions, the mean happens to be equal to the variance. 
On average, each hour, 14 daytraders in the world will go broke. 
Assuming the time each trader goes broke is i.i.d., approximate the chance that 
between 2300 and 2400 will go broke next week.

==> Q4: The probability that between 2300 and 2400 will go broke next week =  0.697328769404


"""
def Q4():
        r = 14*24*7   # the aver rate that #trader go broke next week
        ans = poisson.cdf(2400,r)  -  poisson.cdf(2300,r) ;
        print "Q4: The probability that between 2300 and 2400 will go broke next week = ", ans  ;


"""
5. During each trading hour, stock in “Pink Flamingoes and Garden Gnomes R Us” has a 25% chance of 
losing a dollar, a 25% chance of staying the same, and a 50% chance of gaining 50 cents. 

Approximate the chance that the stock will neither gain nor lose a total of more than 10 dollars over 
the next 300 trading hours

==> 
u= 0.25*(-1) + 0.25*0 + 0.5*0.5 = 0
v = 0.25*1 + 0.5*(0.25) = 0.375
p = scipy.stats.norm(u, s).cdf( 10 ) - scipy.stats.norm(u, s).cdf( -10 )

"""
def Q5():
	u= 0.25*(-1) + 0.25*0 + 0.5*0.5  # mean
	v = 0.25*1 + 0.5*(0.25)  # variance
	s = math.sqrt ( v )  # standard deviation
	p = scipy.stats.norm(u, s).cdf( 10 ) - scipy.stats.norm(u, s).cdf( -10 )
	print "Q5: Prob(no gain or lost of >10) = ", p 


"""
6. Download daily data for your favorite stock from the internet. Grab at least 5 years of data. 
Using this data calculate the following using R. 
Write a program to read in your data file and run all the analyses. 
Do not use the command line for conducting the analyses in this question.

(a) What is the mean daily return? Compute the mean annual return. Report both values.

Q6 (a): mean daily return =  -0.000498601218662
Q6 (b): the daily standard deviation of returns =  0.00566626181544

"""

def dailyReturn ( x,y ) :
    return (y-x)/x    # x = S_t and y=S_t-1

def dailyReturnArray ( arr ) :
    prev = arr[0]
    ans = array([])
    for x in arr[1:]:
        y = dailyReturn ( prev, x);
        ans = append(ans, y);
        prev = x;
    return ans



def Q6ce( arr2):
                mu = arr2.mean()
                sigma = arr2.std()
                days = 365
                x = mu + sigma*N.random.randn( days ) # Q6d

                # the histogram of the data
                n, bins, patches = P.hist( [x, arr2], days/10, normed=1)

                # add a 'best fit' line
                y = mlab.normpdf( bins, mu, sigma)
                l = P.plot(bins, y, 'b--', linewidth=1)

                P.xlabel('Smarts')
                P.ylabel('Probability')
                P.title(r'$\mathrm{Histogram\ of\ returns:}\ Blue: Simulated, Green: Real$')
                x1 = mu-3*sigma
                x2 = mu+3*sigma
                delta = (x2-x1)/10.0
                P.axis( [x1, x2, 0, 125] ) 
                P.grid(True)
                P.show()

def Q6f():
        fn = 'data.txt'
        arr = loadtxt(fn,unpack=True,usecols=[3 ]) # daily closing price 
        arr2 = dailyReturnArray (arr)
	#print arr
	#print arr2
        mu = arr2.mean()
        sigma = arr2.std()
        ans =  scipy.stats.norm(mu, sigma).cdf(-0.1)
        print "Q6(f) Prob. (return <= -0.1) = ", ans

def Q6g():
        fn = 'data.txt'
        arr = loadtxt(fn,unpack=True,usecols=[3 ]) # daily closing price 
        arr2 = dailyReturnArray (arr)
        nTrials = 1000
        sum = 0.0 ;
        for i in range( nTrials ):
                x = average ( N.random.choice(arr2, 20)  )
                if ( x < -0.1):
                         sum = sum + 1;
        print "Q6(g): BootStrap: Prob = ", sum/nTrials               

def Q6(): 
                fn = 'data.txt'  
                arr = loadtxt(fn,unpack=True,usecols=[3 ]) # daily closing price 
                arr2 = dailyReturnArray (arr); 
                print "Q6 (a): mean daily return = ", arr2.mean() 
                print "Q6 (b): the daily standard deviation of returns = ", arr2.std() 
                print "Q6 (b): the annual standard deviation of returns = need 5 years of data" 
                Q6f()
                Q6g()               
                print "Q6 (d): need 5 years of data" 
                print "Q6 (c)(e) see the displayed histogram. Both data corelates."
                Q6ce(arr2)
 


"""
(b) Compute the daily standard deviation of returns, and the annual standard deviation as well.
"""

"""
(c) Assuming that the returns are normally distributed, simulate a histogram of the returns
on the stock for a horizon of 1 year.  Choose a suitable number of random draws from the distribution of returns.
"""

"""
(d) Repeat the analysis for the same stock using a horizon of 5 years. Compare the graph in this question with the one 
from the previous question. What can you say about the two graphs?


"""

"""
(e) Convert each daily return into an annualized value, thereby generating a time series of
annualized returns. Now plot the histogram of this time series.
Overlay this graph on the one from question 6c. 
	Explain what you observe from this comparison.
	What can you say about the normality assumption?
"""

"""
(f) Using the mean and variance you calculated previously for daily returns, calculate the
probability that the stock will  return -10% or worse after 20 trading days.
Use the normal distribution for your calculation.

"""

"""
(g) Bootstrap: You will now undertake a simulation using the original data to calculate the
probability that a stock will lose at least  10% of its value in 20 trading days. One sample draw is
as follows – 
    randomly select 20 of the returns from the downloaded data.
    Sum the  to see if they are −10% or less. 
    Repeat this 100,000 times. Keep track of how many times the condition is satisfied to
    determine the answer   to the question. 
    (This is known  as bootstrapping from empirical data). Compare your answer to
    that of the previous question. Explain what you find.  (Note: answers will vary depending on the stock that you downloaded).
"""
Q1()
Q3()
Q4()
Q5()



Q6()
