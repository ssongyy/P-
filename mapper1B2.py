#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
name=['chris paul','james harden','stephen curry','lebron james']
zone=[]
for line in sys.stdin:
    line=line.strip()
    line=line.split('\t')
    if (float(line[-10])-float(line[-5])) >=-51.1 and (float(line[-10])-float(line[-5])) <=-3.6:
        if float(line[-13])>=0 and float(line[-13])<=12:
            zone.append([line[-2],'Z1',line[-4]])
        else:
            zone.append([line[-2],'Z2',line[-4]])
    elif (float(line[-10])-float(line[-5])) >=-3.5 and (float(line[-10])-float(line[-5])) <=44:
        if float(line[-13])>=0 and float(line[-13])<=12:
            zone.append([line[-2],'Z3',line[-4]])
        else:
            zone.append([line[-2],'Z4',line[-4]])
for i in zone:
        if i[0] in name:
            print '%s\t%s'%(i[0]+'_'+i[1],i[2])

