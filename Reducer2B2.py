#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
for line in sys.stdin:
    line=line.strip()
    line=line.split('\t')
    print'%s\t%s'%(line[0],line[1])

