# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:16:22 2023

@author: Evgeniy
"""

global lsys, turtle, counter, d_sys
import py5
from rule import Rule
from lsys import LSystem
from my_turtle import Turtle
from my_turtle import DynamicSystem

counter = 0

def setup():
    global lsys, turtle, d_sys, turtle2, lsys2
    py5.size(900, 900)
    # Создание набора правил для L-системы
    ruleset = [Rule("F", "FF+[+F+G-F]-[-G+F+F]"), Rule("G", "FF+[+F+G]-[-F+G+F]")]
    # Создание экземпляра L-системы
    lsys = LSystem("F", ruleset)
    lsys2 = LSystem("F+F", ruleset)
    # Создание экземпляра класса черепаха
    turtle2 =  Turtle(lsys2.get_sentence(), py5.height/3, py5.radians(43))
    turtle = Turtle(lsys.get_sentence(), py5.height/3, py5.radians(12))
    # Создание экземпляра класса динамическая система
    d_sys = DynamicSystem(lsys.get_sentence(), py5.height/3, py5.radians(12))
    py5.background(255)
  

def draw():
    
    #py5.background(255)
    py5.fill(0)
    # Первичное перемещение экранной матрицы в точку внизу посередине экрана
    # и поворот матрицы на 90 градусов против часовой стрелки (для 
    # формирования древоподобной структуры)
    py5.push_matrix()
    py5.translate(py5.width/3, py5.height)
    py5.rotate(-py5.PI/2)
    # Либо используем рисование черепахой, либо динамической системой
    turtle.render()
    py5.pop_matrix()
    
    py5.push_matrix()
    py5.translate(py5.width/2, py5.height)
    py5.rotate(-py5.PI/2)
    # Либо используем рисование черепахой, либо динамической системой
    turtle2.render()
    py5.pop_matrix()
    #d_sys.render()
    
    py5.no_loop()


def mouse_pressed():
    global counter
    #Проверяем сколько раз проводили генерацию нового поколения L-системы
    if (counter < 6):
        py5.push_matrix()
        # Генерируем новое поколение L-системы
        lsys.generate()
        lsys2.generate()
        # Строка для отладки - вывод нового поколения в консоль
        #print(lsys.get_sentence())
        # Задаем новое задание либо черепахе, либо дин. системе и уменьшаем
        # размер отрисовки (длину линии или размеры объектов)
        
        turtle.set_todo(lsys.get_sentence())
        turtle.change_len(0.42)
        turtle.change_stroke(0.82)
        turtle2.set_todo(lsys2.get_sentence())
        turtle2.change_len(0.52)
        turtle2.change_stroke(0.92)
        #d_sys.set_todo(lsys.get_sentence())
        #d_sys.change_len(0.42)
        py5.pop_matrix()
        # Вызываем однократное выполнение функции draw()
        py5.redraw()
        # Наращиваем счетчик генераций
        counter += 1

py5.run_sketch()