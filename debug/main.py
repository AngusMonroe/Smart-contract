__author__='XJX'
__date__='2018.02.08'
# -*- coding: utf-8 -*-

from doc2txt import *
from regular_expression import *
import logging

if __name__=='__main__':
    mypath = '/Users/xujiaxing/Documents/GitHub/Smart-contract/data/datadir'
    aimpath = Translate(mypath)
    Extract(aimpath)
