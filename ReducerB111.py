#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from collections import defaultdict
dictt=defaultdict(list)
for line in sys.stdin:
    line = line.strip()
#         print(line)##移除字符的回车 变成了[00:00]5.108.86.176  1 strip(\n)的作用就是把本来一一行一行的，全部连在一起
    team,score = line.split('\t')
    player,defender=team.split('_')
#         print(player,defender,score)
    finalscore=score+'_'+defender
#         print(player,finalscore)
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
#             print(defender)
        score=float(w[0])
        if score>=a:
            a=score
            team=defender
            teamlist.append(team)
        if score<a:
            break
    print'%s\t%s' %(i,teamlist)

