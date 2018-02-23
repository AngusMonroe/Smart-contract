__author__='XJX, LW'
__date__='2018.02.23'
# -*- coding: utf-8 -*-

from doc2txt import *
from regular_expression import *
from keywords import *
import logging

if __name__=='__main__':
    mypath = r'../data/datadir/newdir/租赁合同.txt'
    Extract(mypath)
    Keywords()
