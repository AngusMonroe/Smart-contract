#coding:utf-8
__author__='XJX'
__date__='2018.02.06'

import jieba
import jieba.analyse
import os
import codecs
import sys
import importlib 

in_text = r"/Users/xujiaxing/Documents/GitHub/Smart-contract/data/data.txt"
out_text = r"/Users/xujiaxing/Documents/GitHub/Smart-contract/data/out.txt"

f1 = open(in_text,'r',encoding='utf8')
f2 = open(out_text,'a',encoding='utf8')
jieba.load_userdict("/Users/xujiaxing/Documents/GitHub/Smart-contract/data/userdict.txt")
stoplist = {}.fromkeys([ line.strip() for line in open("/Users/xujiaxing/Documents/GitHub/Smart-contract/data/stopwords.txt") ])

for lines in f1.readlines():
    try:
        tags = jieba.analyse.extract_tags(lines,topK=10, withWeight=False)
        #tags = [word.encode('utf-8') for word in list(tags)]
        tags = [word for word in list(tags) if word not in stoplist]
        print(tags)
        f2.write(str(tags)+'\n')
    except Exception:
        print('error')
        #print(line)
        continue

f1.close()
f2.close()

