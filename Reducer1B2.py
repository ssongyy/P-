#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from collections import defaultdict
from operator import itemgetter
names= defaultdict(list)
pp=defaultdict(list)
ply=defaultdict(list)
for line in sys.stdin:
    line=line.strip('\n')
    line=line.split('\t')
    names[line[0]].append(float(line[1]))
for k,v in names.items():
    pp[k].append(sum(v)/len(v))
for k in pp.keys():
    name,zone=k.split('_')
    ply[name].append([zone,pp[k]])
for k,v in ply.items():
    for i in v:
        if float(i[1][0])>=a:
            a=float(i[1][0])
            b=i[0]
    print '%s\t%s'%(k,b)

