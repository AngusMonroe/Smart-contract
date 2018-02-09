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

def Extract(aimpath):
    in_text = aimpath
    out_text = r"../data/keyword.txt"
    data_text = r"../data/data.txt"

    f1 = open(in_text,'r+',encoding='utf8')
    f2 = open(out_text,'w',encoding='utf8')
    f3 = open(data_text, 'w', encoding='utf8')

    for line in f1.readlines():
        try:
            linkre1 = re.findall("_+(\d+)_+年_+(\d+)_+月_+(\d+)_+日", line)#处理日期格式
            for key in linkre1:
                date = key[0] + '年' + key[1] + '月' + key[2] + '日'
                #print(date)
                date_tran = re.sub('_+(\S*)_+日', '__' + date + '__', line)
                #print(date_tran)
                #print(line)
                line = line.replace(line, date_tran)
                #print(line)
            linkre2 = re.findall("_+([^_]*)_+",line)
            if linkre2:
                print(linkre2)
                for keyword in linkre2:
                    if keyword:
                        f2.write(keyword+'\n')
            f3.write(line)
            line = f1.readline()
        except Exception:
            print('error')
            #print(line)
            #line = f1.readline()
            continue

    f1.close()
    f2.close()
    f3.close()

