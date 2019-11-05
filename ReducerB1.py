
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from collections import defaultdict
dic=defaultdict(list)
for line in sys.stdin:
       line = line.strip('\n') ##移除字符的回车 变成了[00:00]5.108.86.176  1 strip(\n)的作用就是把本来一一行一行的，全部连在一起
       team,score = line.split('\t')
       player,defender=team.split('_')
        #print(player,defender,score)
       finalscore=score+'_'+defender
        #print(finalscore)
       dic[player].append(finalscore)
for i in dic:
        list=[]
        for e in dic[i]:
            list.append(e.split('_'))
        list.sort(reverse = True)
        max=0
        teamlist=[]
        for w in list:
            defender=w[1]
            score=float(w[0])
            if score>=max:
                max=score
                team=defender
                teamlist.append(team)
            if score<max:
                break
        print'%s\t%s' %(i,teamlist)
