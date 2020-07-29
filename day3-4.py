# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:38:15 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
 #小挑戰：斜的道路(X軸)
x,y,z = mc.player.getTilePos()
for i in range(20):
    mc.setBlock(x+i,y-1,z+i,57)
    mc.setBlock(x+i+1,y-1,z+i,57)
    mc.setBlock(x+i+2,y-1,z+i,57)