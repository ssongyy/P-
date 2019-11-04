#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#mapper
import sys
time=[]
for line in sys.stdin:
    line=line.strip()
    line=line.split('\t')
    time.append(line[-9])
for t in time:
    print '%s\t%s' % (t,1)