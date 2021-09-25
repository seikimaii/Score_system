
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 15:17:52 2021

@author: seikimaii
"""
import loadfile as LF
import Rank
import ShowGrade as SG
import changeweight as CW
while True:
    try:
        start = input('請輸入ID或離開(Q):')
        if  start != 'Q' and start not in LF.IDS.keys():
            raise Exception('請重新輸入！只接受Q或ID(長度為10的純數組)')
        elif start == 'Q':
            print('結束查詢') 
            #return 
        else : break
    except Exception as e:
        print('輸入錯誤！',e)
for IDnum,name in LF.IDS.items():
    if start == IDnum:
        student = name
print('welcome,you are looking into %s\'s grade '%(student),end=' ')
while True :
    requirement = input('''
請輸入指令  1) G 顯示成績(Grade)
          2) R 顯示排名(Rank)
          3) W 更新配分(Weight)
          4) E 離開選單(Exit)
          指令： ''')
    if requirement not in 'GRWE':
        print('無效指令！',end=' ')
    elif requirement == 'G':
        SG.getGrade(start)
        pass
    elif requirement == 'R':
        Rank.rank(start)
        pass
    elif requirement == 'W':
        CW.ChangeWeight()
    elif requirement == 'E':
        print('結束查詢')
        break
        

'''

'''