import operator



d = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}
print d

d2 = sorted(d.iteritems(), key=operator.itemgetter(1))
print d2
for x in d2:
    print  x,
    #print "%s" % (x),
print


for key in sorted(d.iterkeys()):
    print "%9s: %s" % (key, d[key]),
print

for x,y in d.items():
    print "%9s: %s" % (x, y),
print


for x in d.keys():
    print "%9s:"  % (x),
print

for x in d.values():
    print "%9d:"  % (x),
print
