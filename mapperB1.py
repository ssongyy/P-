
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from collections import defaultdict
dic=defaultdict(list)
for line in sys.stdin:
    line=line.strip()## 默认删除空白符,去掉空白格
    line=line.split('\t')#按照空格分一下整个数据，一个空格表示一个list 也就是一行是一个list 
    team=line[-1]+'_'+line[-6]
    score=int(line[-4])
    dic[team].append(score)
for i in dic:
    length=len(dic[i])
    totalScore=sum(dic[i])
    rate=1-totalScore/length
    print'%s\t%s' % (str(i),str(rate))

              

