#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:05:56 2021

@author: seikimaii
"""
import sys
import csv
try:
    with open('score.csv',encoding='UTF-8',newline='\n') as score:
        info = csv.reader(score)
        alltable = [row[0:6] for row in list(info)[1:]]
        IDS = {ID[2]:ID[0]+' '+ID[1] for ID in alltable[1:]}
        f = open('weight.txt',mode = 'r')
        weightStr = f.read().split()
        weightElem = [float(i) for i in weightStr] 
        f.close()
except FileNotFoundError:
    print('找不到資料檔案')
    sys.exit()
    
