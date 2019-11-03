#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from operator import itemgetter
import sys
dictc={}
for line in sys.stdin:
    line = line.strip()
    color, count = line.split('\t', 1)
    try:
        count = int(count)
        dictc[color]=dictc.get(color,0)+count
    except ValueError:
        pass
sorted_dictc = sorted(dictc.items(), key=itemgetter(1),reverse=True)
print '%s\t%s' % (sorted_dictc[0][0],sorted_dictc[0][1])

