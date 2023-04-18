#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:09:43 2023

@author: evgeniy
"""

import py5_tools

if not py5_tools.is_jvm_running():
    py5_tools.add_jars("./jars")

import py5
import random
import time


def setup():
    # наша глобальная переменная - массив для хранения сущностей,
    # указываем ее в каждой функции
    global entities, tick
    # указываем размер окна
    py5.size(600, 600)
    # задаем цвет фона
    py5.background(0)
    # создаем пустой список для сущностей
    entities = []
    # цикл для заполнения массива сущностей
    for i in range(30):
        entities.append(
            Entity(
                random.randint(0, 600),
                random.randint(0, 600),
                random.randint(30, 90),
                255,
            )
        )


def draw():
    # наша глобальная переменная - массив для хранения сущностей,
    # указываем ее в каждой функции
    global entities, tick
    # заливаем окно черным цветом, чтобы получить анимацию
    py5.background(0)
    # цикл перебора всех соседних сущностей, чтобы бы изменить диаметры
    for i in range(len(entities) - 1):
        # взяли очередную сущность из списка и делаем вложенный цикл,
        # чтобы определить степень изменения собственного диаметра
        for j in range(len(entities) - 1):
            distance = entities[i].analyze(entities[j])
            entities[i].change(distance)
        entities[i].show()
    # указываем время засыпания 0.1 с
    time.sleep(0.01)


class Entity:
    def __init__(self, x, y, diameter, color):
        self.pos = py5.Py5Vector(x, y)
        self.diameter = diameter
        self.color = color

    def analyze(self, neighbour):
        distance = (
            self.pos.dist(neighbour.pos)
            - self.diameter / 2
            - neighbour.diameter / 2
        )
        return distance

    def change(self, distance):
        if distance < self.diameter / 2:
            self.diameter -= 0.099
        elif distance > self.diameter / 2 and distance < self.diameter * 1.5:
            self.diameter += 0.052192
        elif distance > self.diameter * 3:
            pass
        elif distance == 0:
            pass

    def show(self):
        py5.stroke(0)
        py5.fill(self.color)
        py5.circle(self.pos.x, self.pos.y, self.diameter)


# функция для запуска скетча
py5.run_sketch()
