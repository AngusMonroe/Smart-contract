#coding:utf-8
__author__='XJX'
__date__='2018.02.06'

import jieba
import jieba.analyse
import re
import os
import codecs
import sys
import importlib 

def Keywords():
    in_text = r"../data/data.txt"  # 原合同文本
    map_text = r"../data/map.txt"  # 储存关键词映射
    ans_text = r"../data/ans.txt"  # 储存最终结果

    f1 = open(in_text,'r',encoding='utf8')
    f2 = open(map_text,'r',encoding='utf8')
    f3 = open(ans_text, 'w', encoding='utf8')

    jieba.load_userdict("../data/userdict.txt")
    stoplist = {}.fromkeys([ line.strip() for line in open("../data/stopwords.txt") ])

    #提取map.txt中原有数据
    # lines = []
    # for line in f2:
    #     lines.append(line)
    # f2.close()

    num = 1
    s = []
    line = f1.readline()
    while line:
        try:
            tag = '##' + str(num) +'##'
            print(tag)
            flag = re.findall(tag, line)#匹配标记所在行
            if flag:
                ans = f2.readline()[:-1]

                keys = jieba.analyse.extract_tags(line,topK = 3, withWeight = False)#提取3个关键词
                #keys = [word.encode('utf-8') for word in list(tags)]
                keys = [word for word in list(keys) if word not in stoplist]#去停用词
                print(keys)
                for key in keys:
                    ans += ' ' + str(key)
                f3.write(ans + '\n')

                num += 1

            line = f1.readline()

        except Exception:
            print('error')
            #print(line)
            line = f1.readline()
            continue

    #f2 = open(map_text, 'w+', encoding='utf8')
    #f2.write(s)

    f1.close()
    f2.close()

if __name__ == '__main__':
    Keywords()