def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    return -1

def do_binary_search(a, key):
    n = len(a);
    x = binary_search(a,key,0,n);
    if (x>=0 ):
        print "find a[%d]: %d" % (x, a[x])
    else:
        print "Cannot find %d." %(key)    


a=[1,2,3,4,5,6,7]
  
from random import randint


for x in range(0, 10):
    print "Iteration %d:" % (x), 
    key = randint(2,9)
    do_binary_search(a,key)


