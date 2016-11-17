import operator

x={'Rahul' : {'score' : 75},'Suhas' : {'score' : 95},'Vanita' : {'score' : 56}, 
   'Dinesh' : {'score' : 78},'Anil' : {'score' : 69},'Anup' : {'score' : 95} 
  }
sorted_x = sorted(x.iteritems(), key=operator.itemgetter(1))
#print sorted_x


d = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

sorted_x = sorted(d.iteritems(), key=operator.itemgetter(1))
print sorted_x
