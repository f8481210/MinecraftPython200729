# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:43:21 2020

@author: User
"""

#小挑戰：蓋出一個平面的樹
#z+?
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def plantree (x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,22)#樹葉
    mc.setBlocks(x,y,z,x,y+4,z,17) #樹幹
    
x,y,z = mc.player.getTilePos()
for i in range(10):
    for j in range(5):
        for k in range(5):
            plantree(x+7*i,y+k*7,z+j*7) #第一行
    #plantree(x+7*i,y,z+7) #第二行
    #plantree(x+7*i,y,z+14) #第三行
    #plantree(x+7*i,y,z+21) #第四行
    #plantree(x+7*i,y,z+28) #第五行
    