#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import sys
newlist=[]
for line in sys.stdin:
    line=line.strip()
    line=line.split('\t')
    newitem=line[-2]+'--'+line[6]
    newlist.append(newitem)
for i in newlist:
    print '%s\t%s' % (i,1)
