
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import sys

from collections import defaultdict
dic=defaultdict(list)
for line in sys.stdin:  
        line = line.strip() ##移除字符的回车 变成了[00:00]5.108.86.176  1 strip(\n)的作用就是把本来一一行一行的，全部连在一起
        line = line.strip('\t')
        fight,score=line.split(' ')
        team,defender=line.split('_')
        dic[team].append(defender)
for i in dic:
        result=[]
        for e in dic[i]:
            item=e[-3:]+' '+e[:-3]
            result.append(item)
        result.sort(reverse = True)
        max=0
        teamlist=[]
        for W in result:
            rate=float(W[0:3])
            team=W[3::]
            if rate>=max:
               max=rate
               team=W[3::]
               teamlist.append(team)
            if rate<max:
               break
        print '%s\t%s' %(i,teamlist)
    
