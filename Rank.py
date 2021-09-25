#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 17:48:41 2021

@author: seikimaii
"""
import AlltempData as AD
import loadfile as LF
import numpy as np
def rank(ID):
    allscore = np.zeros((len(LF.alltable),len(LF.alltable[0])-3))
    for i in range(len(LF.alltable)):
        for j in range(len(LF.alltable[0])-3):
            allscore[i][j] = int(LF.alltable[i][j+3])
    allscore[:,0] *= AD.weight['mathweight']
    allscore[:,1] *= AD.weight['englisgweight']
    allscore[:,2] *= AD.weight['computerweight']
    H,W = allscore.shape
    weightscore = np.array([allscore[i].sum() for i in range(H)])
    weightscore = weightscore.round()
    rank = {LF.alltable[i][2]:weightscore[i] for i in range(len(weightscore))}
    rank = sorted(rank.items(),key = lambda x:x[1],reverse=True)
    for IDnum in range(len(rank)):
        if rank[IDnum][0] == ID:
            if IDnum == 0:
                print('第%d名'%(IDnum+1),'(%d/%d)'%(IDnum+1,len(rank)),end=' ')
            else:
                if rank[IDnum][1] == rank[IDnum - 1][1]:
                    print('第%d名'%(IDnum+1),'(%d/%d)'%(IDnum+1,len(rank)),'與上一名同分',end=' ')
                else:
                    print('第%d名'%(IDnum+1),'(%d/%d)'%(IDnum+1,len(rank)),end=' ')


