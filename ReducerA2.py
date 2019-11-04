#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from operator import itemgetter
import sys
dict_ip_count = {}
 ## 这就是我们跑出来的。。最后的文档。。。 
for line in sys.stdin:
        line = line.strip('\n') ##移除字符的回车 变成了[00:00]5.108.86.176	1 strip(\n)的作用就是把本来一一行一行的，全部连在一起
        yearC,num= line.split('\t')
        try:
            num = int(num)
            dict_ip_count[yearC] = dict_ip_count.get(yearC, 0) + num
        except ValueError:
            pass

year_type=[]
sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(1),reverse=True)

for i in sorted_dict_ip_count:
     if i[0][0]!='0':
        year_type.append(i)
print '%s\t%s' % (year_type[0])
      