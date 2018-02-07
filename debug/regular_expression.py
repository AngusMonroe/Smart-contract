#coding:utf-8
__author__='XJX'
__date__='2018.02.07'

import jieba
import jieba.analyse
import os
import re
import codecs
import sys
import importlib 

in_text = r"/Users/xujiaxing/Documents/GitHub/Smart-contract/data/data.txt"
out_text = r"/Users/xujiaxing/Documents/GitHub/Smart-contract/data/keyword.txt"

f1 = open(in_text,'r',encoding='utf8')
f2 = open(out_text,'a',encoding='utf8')

for lines in f1.readlines():
    try:
        #linkre = re.compile("_*(.*?)_*")
        linkre = re.findall("_+([^_]*)_+",lines)
        if linkre:
            print(linkre)
            for keyword in linkre:
                f2.write(keyword+'\n')
    except Exception:
        print('error')
        #print(line)
        continue

f1.close()
f2.close()

