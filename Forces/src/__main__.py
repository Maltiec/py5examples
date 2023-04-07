# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:43:12 2023

@author: Evgeniy
"""

import py5
import random
import circle_vects

def setup():
    global x_coord, y_coord, my_circle, another_circle, mu, normal
    py5.size(500, 500)
    py5.background(0)
    py5.stroke(255, 0, 0)
    py5.fill(255, 0, 0)
    x_coord = 60
    y_coord = 60
    my_circle = circle_vects.Circle(50, 50)
    another_circle = circle_vects.Circle(70, 150)
    #gravity_force = py5.Py5Vector(0, 0.8)
    mu = 0.1
    normal = 1
    #py5.no_loop()


def draw():
    global x_coord, y_coord, my_circle, another_circle, mu, normal
   
    #Перемещение двух экземпляров класса Circle
    py5.background(0)
    
    """
    # аттрактором является курсор мыши
    mouse_point = py5.Py5Vector(py5.mouse_x, py5.mouse_y)
    force1 = mouse_point - my_circle.position
    force1 = force1.norm * 0.03
    force2 = mouse_point - another_circle.position
    force2 = force2.norm * 0.03
    my_circle.apply_force(force1)
    another_circle.apply_force(force2)
    """
    
    """
    # Вычисляем силу тяготения (то что тянет объекты вниз)
    gravity_force1 = py5.Py5Vector(0, 0.8 * my_circle.mass)
    my_circle.apply_force(gravity_force1)
    # Вычисляем силу трения (постепенно она затормозит объект)
    friction1 = my_circle.velocity.copy
    friction1.normalize()
    friction1 *= -1
    friction1 *= mu * normal
    my_circle.apply_force(friction1)
    """
    
    """
    # Вычисляем силу тяготения (то что тянет объекты вниз)
    gravity_force2 = py5.Py5Vector(0, 0.8 * another_circle.mass)
    another_circle.apply_force(gravity_force2)
    # Вычисляем силу трения (постепенно она затормозит объект)
    friction2 = another_circle.velocity.copy
    friction2.normalize()
    friction2 *= -1
    friction2 *= mu * normal
    another_circle.apply_force(friction2)
    """
    
    # Прилагаем силу гравитации
    force = gravity_force(my_circle, another_circle)
    #my_circle.apply_force(force)
    another_circle.apply_force(force)
    my_circle.move()
    another_circle.move()
    my_circle.check_edges()
    another_circle.check_edges()
    my_circle.display()
    another_circle.display()
    
"""
Функция для вычисления силы гравитационного взаимодействия двух объектов
"""
def gravity_force(object1, object2):
    direction = object1.position - object2.position
    distance = direction.mag
    distance = py5.constrain(distance, object1.diameter / 2 +  object2.diameter / 2, 150)
    direction.normalize()
    amplitude = (0.1 * object1.mass * object2.mass)/(distance * distance)
    force = direction * amplitude
    return force
"""
Функция для реакции на нажатие клавиши мыши
"""
def mouse_clicked(e):
    wind = py5.Py5Vector(0.5, 0)
    my_circle.apply_force(wind)
    another_circle.apply_force(wind)
    
py5.run_sketch()