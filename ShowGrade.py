#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 01:13:54 2021

@author: seikimaii
"""
import loadfile as LF
import AlltempData as AD
def getGrade(ID):
    for i in range(len(LF.alltable)):
        for j in range(len(LF.alltable[0])-3):
            LF.alltable[i][j+3] = int(LF.alltable[i][j+3])
    for row in LF.alltable:
        if row[2] == ID:
            t_score = (row[3]*AD.weight['mathweight'] + row[4]*AD.weight['englisgweight']+row[5]*AD.weight['computerweight'])
            t_score = round(t_score)
            print('''
math:%17d (%.2f)
english:%14d (%.2f)
computer science:%5d (%.2f)
final score: %9d'''%(row[3],AD.weight['mathweight'],row[4],AD.weight['englisgweight'],row[5],AD.weight['computerweight'],t_score),end=' ')
              
