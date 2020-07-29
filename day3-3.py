# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:05:17 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time,random


while True:
    pos = mc.player.getPos()
    x = pos.x+random.uniform(-20,20)
    z = pos.z+random.uniform(-20,20)
    y = pos.y+30
    mc.spawnEntity(x,y,z,20)
    time.sleep(0.5)
