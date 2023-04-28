# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:04:37 2023

@author: Evgeniy
"""

import py5

def setup():
    py5.size(1000,1000)
    py5.background(255)
    py5.stroke(0)
    py5.fill(127)

def draw():
    py5.translate(500, 500)
    drawCircle(0,0,500, 127)
    py5.no_loop()
    
def drawCircle(x, y, radius, col): 
    py5.stroke(0)
    py5.fill(col)
    py5.ellipse(x, y, radius, radius)
    """
    if radius > 2:
        drawCircle(x + radius/2, y, radius/2)
        drawCircle(x - radius/2, y, radius/2)
    """
    if radius > 8:
        drawCircle(x + radius/2, y, radius/2, col/2)
        drawCircle(x - radius/2, y, radius/2, col*2)
        drawCircle(x, y + radius/2, radius/2, col/2)
        drawCircle(x, y - radius/2, radius/2, col*2)

py5.run_sketch()