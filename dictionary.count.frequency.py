import operator


#given a list, find the occurring frequency of each word
list = ["xxx","xxx", "s", "xx" ]
d = {}

phonebook = {'Andrew Parson':8806336, \
'Emily Everett':6784346, 'Peter Power':7658344, \
'Lewis Lame':1122345, 'Andrew Parson':1234567}

for s in list:
    d[s] = 0


for s in list:
    if d.has_key(s):
        d[s] = d[s]+1
    else:
        d[s]=0

for k in sorted(d.iterkeys()):
    print "%9s: %s" % (k, d[k]),
print



if 'yyy' in d.keys():
  print "blah"
else:
  print "boo"


for name, f in d.items():
    if f == 2:
        print name, str(f)
