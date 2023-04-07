# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 18:06:44 2023

@author: Evgeniy
"""

import py5


def setup():
    global entity1, entity2
    py5.size(500, 500)
    py5.background(0)
    py5.stroke(255)
    py5.fill(255)
    entity1 = Entity(py5.random(500), py5.random(500))
    entity2 = Entity(py5.random(500), py5.random(500))
    
def draw():
    global entity1, entity2
    py5.background(0)
    entity1.display()
    entity2.display()
    
    
class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.diameter = py5.random(80)
    
    def life_process(self):
        pass
    
    def display(self):
        py5.push_matrix()
        py5.translate(self.x, self.y)
        py5.circle(0, 0, self.diameter)
        py5.pop_matrix()


py5.run_sketch()