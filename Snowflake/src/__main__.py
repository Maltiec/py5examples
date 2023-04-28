# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:59:29 2023

@author: Evgeniy
"""
import py5

global MIN_DEPTH, MAX_DEPTH

MIN_DEPTH = 2
MAX_DEPTH = 9
def setup():
    py5.size(1000,1000)
    py5.background(255)
    seed1 = Vector(200,40,300,120)
    fractal(seed1,MAX_DEPTH)
    seed2 = Vector(350,300,300,-120)
    fractal(seed2,MAX_DEPTH)
    seed3 = Vector(50,300,300,0)
    fractal(seed3,MAX_DEPTH)
        

class Vector:
    def __init__(self, x, y, r, theta):
        self.x = x
        self.y = y
        self.r = r
        self.theta = theta
        
    def getEndX(self):
        return self.x + self.r * py5.cos(py5.radians(self.theta))
    
    def getEndY(self):
        return self.y + self.r * py5.sin(py5.radians(self.theta))
    
    def drawVector(self):
        py5.line(self.x, self.y, self.getEndX(), self.getEndY())


def fractal(v, N):
    if (N == 0): 
        v.drawVector()  #Draw the current vector
    else: 
        t1 = Vector(v.x,v.y,v.r/3.0,v.theta)
        t2 = Vector(t1.getEndX(), t1.getEndY(), v.r/3.0, v.theta + 60.0)
        t3 = Vector(t2.getEndX(), t2.getEndY(), v.r/3.0, v.theta - 60.0)
        t4 = Vector(t3.getEndX(), t3.getEndY(), v.r/3.0, v.theta)
        fractal(t1, N-1)  #Recurse
        fractal(t2, N-1)  #Recurse
        fractal(t3, N-1)  #Recurse
        fractal(t4, N-1)  #Recurse

py5.run_sketch()