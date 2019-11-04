#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#reducer
from operator import itemgetter
dict = {}
for line in sys.stdin:
    line = line.strip('\n') 
    time,num= line.split('\t')
    try:
        num = int(num)
        dict[time] = dict.get(time, 0) + num
    except ValueError:
        pass
sorted_dict = sorted(dict.items(), key=itemgetter(1),reverse=True)

print '%s\t%s' % (sorted_dict[0])


      