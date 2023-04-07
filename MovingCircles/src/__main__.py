# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 13:57:48 2023

@author: Evgeniy
"""

import py5
import random
import circle_vects

def setup():
    global delta_x, delta_y, x_coord, y_coord, my_circle, another_circle
    py5.size(500, 500)
    py5.background(0)
    py5.stroke(255, 0, 0)
    py5.fill(255, 0, 0)
    delta_x = 2
    delta_y = 3
    x_coord = 60
    y_coord = 60
    my_circle = circle_vects.Circle(50, 50)
    another_circle = circle_vects.Circle(70, 150)
    #py5.no_loop()


def draw():
    global delta_x, delta_y, x_coord, y_coord, my_circle, another_circle
    """ 
    #Перемещение без создания экземпляра класса
    py5.push_matrix()
    py5.translate(x_coord, y_coord)
    py5.circle(0, 0, 80)
    py5.pop_matrix()
    if x_coord + 40 > 500:
        delta_x = - delta_x
        x_coord = 460
    if x_coord - 40 < 0:
        delta_x = - delta_x
        x_coord = 40
    if y_coord + 40 > 500:
        delta_y = - delta_y
        y_coord = 460
    if y_coord - 40 < 0:
        delta_y = - delta_y
        y_coord = 40
    print(delta_y)
    x_coord += delta_x
    y_coord += delta_y
    """
    
    
    #Перемещение двух экземпляров класса Circle
    py5.background(0)
    mouse_point = py5.Py5Vector(py5.mouse_x, py5.mouse_y)
    force1 = mouse_point - my_circle.position
    force1 = force1.norm * 0.03
    force2 = mouse_point - another_circle.position
    force2 = force2.norm * 0.03
    my_circle.apply_force(force1)
    another_circle.apply_force(force2)
    my_circle.move()
    another_circle.move()
    my_circle.check_edges()
    another_circle.check_edges()
    my_circle.display()
    another_circle.display()
    
    
    """
    #равномерное распределение
    for i in range(50000):
        py5.point(py5.random_int(0, 500), py5.random_int(0, 500))
    """
    """
    #гауссовское распределение
    for i in range(10000):
        py5.point(py5.random_gaussian(250, 20), py5.random_gaussian(250, 100))
    

    #перлиновский шум
    py5.noise_detail(12, 0.75)
    py5.point(py5.noise(py5.frame_count / 100) * 200, py5.noise(py5.frame_count / 130) * 200) 
    """

py5.run_sketch()
