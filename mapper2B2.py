#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from collections import defaultdict
a=0
ply=defaultdict(list)
for line in sys.stdin:
    line=line.strip()
    line=line.split('\t')
    name,zone=line[0].split('_')
    ply[name].append([zone,line[1]])
for k,v in ply.items():
    for i in v:
        if float(i[1])>=a:
            a=float(i[1])
    for i in v:
        if float(i[1])==a:
            print'%s\t%s'%(k,i[0])

