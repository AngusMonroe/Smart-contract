__author__='XJX, LW'
__date__='2018.02.23'
# -*- coding: utf-8 -*-

from doc2txt import *
from regular_expression import *
from keywords import *
import logging

def nlp():
    mypath = r'../data/datadir'
    aimpath = Translate(mypath)
    Extract(aimpath)
    Keywords()

if __name__=='__main__':
    nlp()
