# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:19:28 2023

@author: Evgeniy
"""
import py5

def setup():
    global newTree
    py5.size(1000,1000)
    py5.background(0)
    py5.stroke(255)
    newTree = Htree()

def draw():
    global newTree
    newTree.drawHTree(4,500,500,500)

class Htree:
    def __init__(self):
        dummy = 0
    
    def drawHTree(self, n, sz, x, y):
        if n == 0:
            return
        x0 = x - sz/2
        x1 = x + sz/2
        y0 = y - sz/2
        y1 = y + sz/2
        py5.line(x0, y, x1, y)
        py5.line(x0, y0, x0, y1)
        py5.line(x1, y0, x1, y1)
        self.drawHTree(n-1, sz/2, x0, y0)
        self.drawHTree(n-1, sz/2, x0, y1)
        self.drawHTree(n-1, sz/2, x1, y0)
        self.drawHTree(n-1, sz/2, x1, y1)

py5.run_sketch()