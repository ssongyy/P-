#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
color=[]
for line in sys.stdin:
    line=line.strip()
    line=line.split('\t')
    color.append(line[-3])
for p in color:
    print "%s\t%s" % (p,1)

