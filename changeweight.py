#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 20:20:13 2021

@author: seikimaii
"""
import Exception
import AlltempData as AD
def ChangeWeight():
    while True:
        try:
            New_weight = input('''目前配分
            math   %14.2f
            englisg  %12.2f 
            computer science%5.2f
            退出請輸入Q
            請輸入配分：'''
            %(AD.weight['mathweight'],AD.weight['englisgweight'],AD.weight['computerweight']))
            if New_weight == 'Q':
                break
            New_weight = New_weight.split(sep=' ')
            New_weight = [float(elem) for elem in New_weight if float(elem) >=0]
            
            if len(New_weight) != 3:
                raise Exception.weightNumError
            if sum(New_weight) < 0.99:
                raise Exception.weightSumError
        except Exception.weightSumError :
            print('總和必須為1')
        except ValueError:
            print('請輸入0~1之間的數值作為權重')
        except Exception.weightNumError :
            print('期望3個正數值,卻收到%d個'%(len(New_weight)))   
        else:
            AD.weight = {'mathweight' : New_weight[0],'englisgweight' : New_weight[1],'computerweight' : New_weight[2]}
            file = open('weight.txt',mode = 'w')
            file.write(str(New_weight[0])+' '+str(New_weight[1])+' '+str(New_weight[2]))
            file.close()

            print('權重分配成功')    
            break
