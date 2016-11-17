import operator




d = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

for k in sorted(d.iterkeys()):
    print "%9s: %s" % (k, d[k]),
print

for k in sorted(d):
    print k,
    print  d[k], # gives the values sorted by key
print



x = sorted(d.iteritems(), key=operator.itemgetter(1))
print d
print x


"""

for v in sorted(d.values()):
    print v, # gives the values sorted by value
print 










"""

#from collections import OrderedDict
#from operator import itemgetter

#d = OrderedDict(sorted(d.items(), key=itemgetter(1)))
#print d
