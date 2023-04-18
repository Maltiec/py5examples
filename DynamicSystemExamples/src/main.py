#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 09:11:27 2023

@author: evgeniy
"""

import py5


def setup():
    global test_sq, test_sq2, squares_list
    py5.size(500, 500)
    py5.background(0)
    # Создаем объекты
    #test_sq = RotatingSquare(250, 250, 40, 0.1)
    #test_sq2 = RotatingSquare(100, 250, 40, 0.02)
    squares_list = []
    for i in range(50):
        squares_list.append(RotatingSquare(py5.random(500), py5.random(500), 40,py5.random(0.1, 0.7)))

def draw():
    global test_sq, test_sq2, squares_list
    # Заливаем фон черным
    py5.background(0)
    # Изменяем состояние объектов системы
    #test_sq.change_state(test_sq2)
    #test_sq2.change_state(test_sq)
    # Отрисовываем объекты системы
    #test_sq.show()
    #test_sq2.show()
    for i in range(len(squares_list)):
        if i != 0:
            squares_list[i].change_state(squares_list[i-1])
            squares_list[i].show()


"""
Класс RotatingSquare

self.pos - вектор местоположения
self.size - размер стороны квадрата
self.speed - скорость вращения объекта
self.angle - текущий угол поворота объекта
"""


class RotatingSquare:
    def __init__(self, x, y, size, speed):
        self.pos = py5.Py5Vector(x, y)
        self.size = size
        self.speed = speed
        self.angle = 0

    def change_state(self, neighbour):
        
        distance = self.pos.dist(neighbour.pos)
        if distance > 100:
            self.speed += 0.02
            self.size -= 0.01
        if distance > 100 and neighbour.speed > 0.3:
            self.speed -= 0.05
        if (neighbour.speed + self.speed) > 0.062:
            self.speed -= 0.08
        
        # Наращиваем угол поворота объекта на его скорость вращения
        self.angle += self.speed

    def show(self):
        py5.push_matrix()
        #
        py5.rect_mode(py5.CENTER)
        #
        py5.translate(self.pos.x, self.pos.y)
        #
        py5.rotate(py5.radians(self.angle))
        py5.square(0, 0, -self.size)
        py5.pop_matrix()


py5.run_sketch()
