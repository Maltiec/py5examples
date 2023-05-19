# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:17:06 2023

@author: Evgeniy
"""

import py5

"""
Класс Turtle

При создании задаем параметры:
    
    todo - последовательность команд для исполнения черепахой
    tLen - длина линии, которую рисует черепаха
    theta - угол на который поворачивается черепаха

    Методы:
        
        render - выполнение команд из строки self.todo
        
        set_len(l - длина в пикселах) - задать длину линий 
        
        change_len(percent - изменение в процентах) - изменить длину линии 
        
        set_todo(s - строка с символами) - задать последовательность
        
        change_stroke(percent - изменение в процентах) - изменить толщину линии
"""

class Turtle:
    def __init__(self, todo, tLen, theta):
        self.todo = todo
        self.tLen = tLen
        self.theta = theta
        self.t_stroke = 4

    def render(self):
        py5.stroke(0, 175)
        py5.stroke_weight(self.t_stroke)
        for i in range(0, len(self.todo), 1):
            curr_char = self.todo[i]
            #
            if curr_char == 'F':
                py5.line(0, 0, self.tLen, 0)
                py5.translate(self.tLen, 0)
            elif curr_char == 'G':
                py5.line(0, 0, 0, self.tLen)
                py5.translate(0, self.tLen)
            elif curr_char == '+':
                py5.rotate(self.theta)
            elif curr_char == '-': 
                py5.rotate(-self.theta)
            elif curr_char == '[': 
                py5.push_matrix()
            elif curr_char == ']':
                py5.pop_matrix()
    
    def set_len(self, l):
        self.tLen = l

    def change_len(self, percent):
        self.tLen *= percent

    def set_todo(self, s):
        self.todo = s
    
    def change_stroke(self, percent):
        self.t_stroke *= percent

"""

"""

class DynamicSystem:
    def __init__(self, todo, tLen, theta):
        self.todo = todo
        self.tLen = tLen
        self.theta = theta

    def render(self):
        py5.stroke(0, 175)
        for i in range(0, len(self.todo), 1):
            curr_char = self.todo[i]
            #
            if curr_char == 'F':
                py5.circle(0, 0, self.tLen)
                py5.translate(self.tLen * 1.3, self.tLen)
            elif curr_char == 'G':
                py5.square(0, 0, self.tLen / 1.3)
                py5.translate(0, self.tLen * 1.4)
            elif curr_char == '+':
                py5.rotate(self.theta)
            elif curr_char == '-': 
                py5.rotate(-self.theta)
            elif curr_char == '[': 
                py5.push_matrix()
            elif curr_char == ']':
                py5.pop_matrix()
    
    def set_len(self, l):
        self.tLen = l

    def change_len(self, percent):
        self.tLen *= percent

    def set_todo(self, s):
        self.todo = s