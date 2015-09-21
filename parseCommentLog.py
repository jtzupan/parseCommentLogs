# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:13:32 2015

@author: johnzupan
"""
import re

def readInFile(fileName):
    print 'Starting to read file\n'
    openedFile = open(fileName, 'rb+')
    searchPattern = re.compile(r'("[\w]*")')    
    for line in openedFile:
        x = line.strip('\r\n').split('/')
        searchPattern.findall(x)
#        print x[0], x[2], x[4], x[5] 
#        userIPTuple = {(x[0],x[1]): (x[4], x[5]) for x in line.strip('\r\n').split('/')}
    print '\nFinished reading file'
#    print userIPTuple