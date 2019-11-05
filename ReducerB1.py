#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from collections import defaultdict
dictt=defaultdict(list)
for line in sys.stdin:
    line = line.strip()
    team,score = line.split('\t')
    player,defender=team.split('_')
    finalscore=score+'_'+defender
    dictt[player].append(finalscore)
for k,v in dictt.items():
    list1=[]
    for e in v:
        list1.append(e.split('_'))
    list1.sort(reverse = True)
    a=0
    teamlist=[]
    for w in list1:
        defender=w[1]
        score=float(w[0])
        if score>=a:
            a=score
            team=defender
            teamlist.append(team)
        if score<a:
            break
    print'%s\t%s' %(i,teamlist)

