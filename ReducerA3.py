#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from operator import itemgetter
import sys
dictc={}
for line in sys.stdin:
    line = line.strip('\n')
    street, count = line.split('\t', 1)
    try:
        count = int(count)
        dictc[street]=dictc.get(street,0)+count
    except ValueError:
        pass
sorted_dictc = sorted(dictc.items(), key=itemgetter(1),reverse=True)
print('%s\t%s' % (sorted_dictc[0][0],sorted_dictc[0][1]))

