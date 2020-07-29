# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:22:46 2020

@author: User
"""
#小挑戰：只有打到石頭才會變成金礦

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    hits = mc.events.pollBlockHits()
    #判斷方塊是不是被打到
    if len(hits)>0: #判斷有沒有打到東西
        block = hits[0]
        x,y,z = block.pos.x,block.pos.y,block.pos.z
        a = mc.getBlock(x,y,z)
        if a == 1:
            mc.setBlock(x,y,z,41)
        #mc.postToChat("你打到"+str(a))
        #mc.setBlock(x,y,z,41)
    