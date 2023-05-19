# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:56:30 2023

@author: Evgeniy
"""

import py5

class Key:
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.x1 = 0
        self.y1 = 0
        self.x2 = py5.random_int(5, 10)
        self.y2 = 0
        self.x3 = py5.random_int(15, 25)
        self.y3 = 0
        
    
    def show(self):
        py5.push_matrix()
        second_x = self.x1 + py5.random_int(3, 8)
        second_y = self.y1 + py5.random_int(6, 14)
        first_control_x = py5.random_int(5, 20)
        first_control_y = py5.random_int(5, 20)
        second_control_x = py5.random_int(5, 20)
        second_control_y = py5.random_int(5, 20)
        py5.curve(float(first_control_x),
                  float(first_control_y),
                  float(self.x1),
                  float(self.y1),
                  float(second_x),
                  float(second_y),
                  float(second_control_x),
                  float(second_control_y)
                  )
        second_x = self.x2 + py5.random_int(3, 8)
        second_y = self.y2 + py5.random_int(6, 14)
        first_control_x = py5.random_int(5, 20)
        first_control_y = py5.random_int(5, 20)
        second_control_x = py5.random_int(5, 20)
        second_control_y = py5.random_int(5, 20)
        py5.curve(float(first_control_x),
                  float(first_control_y),
                  float(self.x2),
                  float(self.y2),
                  float(second_x),
                  float(second_y),
                  float(second_control_x),
                  float(second_control_y)
                  )
        second_x = self.x3 + py5.random_int(3, 8)
        second_y = self.y3 + py5.random_int(6, 14)
        first_control_x = py5.random_int(5, 20)
        first_control_y = py5.random_int(5, 20)
        second_control_x = py5.random_int(5, 20)
        second_control_y = py5.random_int(5, 20)
        py5.curve(float(first_control_x),
                  float(first_control_y),
                  float(self.x2),
                  float(self.y2),
                  float(second_x),
                  float(second_y),
                  float(second_control_x),
                  float(second_control_y)
                  )
        
        py5.pop_matrix()
    
    