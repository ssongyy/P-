#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
street=[]
for line in sys.stdin:
    line=line.strip()
    line=line.split('\t')
    street.append(line[-7])
for p in street:
    print"%s\t%s\n" % (p,1)

