# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import py5

def setup():
    global t, x, y, A1, A2, f1, f2, p1, p2, d1, d2
    py5.size(800, 800)
    py5.background(0)
    py5.stroke(255)
    py5.stroke_weight(1)
    t = 0
    x = 0
    y = 0
    A1 = 10
    A2 = 7
    f1 = 2.1
    f2 = 2.2
    p1 = 0
    p2 = 0
    d1 = 0.05
    d2 = 0.02

def draw():
    global t, x, y, A1, A2, f1, f2, p1, p2, d1, d2
    #py5.background(0)
    py5.push_matrix()
    py5.translate(400, 400)
    py5.rotate(py5.radians(2*t))
    x += A1 * py5.sin(f1 * t + p1) * py5.exp(-d1 * t) 
    y += A2 * py5.sin(f2 * t + p2) * py5.exp(-d2 * t)
    py5.point(x, y)
    t += 0.03
    py5.pop_matrix()

py5.run_sketch()