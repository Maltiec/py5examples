# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:24:11 2023

@author: Evgeniy
"""

import py5


def setup():
    py5.size(1000,1000)
    py5.background(255)
    piet(100,100,900,900,3)

def piet(x0,y0,x1,y1,N):
    if N == 0:
        sw = 3 #Задаем толщину разделительной линии
        c = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ffffff' ] #Создаем список с палитрой возможных цветов
        py5.fill(c[int(py5.random(len(c)))])  #Указываем цвет заполнения на основе случайно выбранного цвета из списка
        py5.stroke_weight(sw)
        py5.rect(x0,y0,x1-x0-sw,y1-y0-sw)
    else:
        i = int(py5.random(x0,x1))
        j = int(py5.random(y0,y1))
        piet(x0,y0,i,j,N-1)
        piet(i,y0,x1,j,N-1)
        piet(x0,j,i,y1,N-1)
        piet(i,j,x1,y1,N-1)

py5.run_sketch()