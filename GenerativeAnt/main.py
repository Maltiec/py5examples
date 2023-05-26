# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:35:19 2023

@author: Evgeniy
"""

import py5
from ant import Ant

def setup():
    global test_ant, ants
    py5.size(900, 500)
    py5.background(255)
    ants = []
    for i in range(10):
        ants.append(Ant(py5.random(0.7, 1.1), py5.random(0.6, 0.9), 2.1, py5.random(5,7), 20))
    
    
    
def draw():
    global test_ant, ants
    for i in range(len(ants)):
        ants[i].show(90 * i, 250)
    #test_ant2.show(100, 100)

py5.run_sketch()