# -*- coding: utf-8 -*-

import py5

class Ant:
    def __init__(self, param1, param2, param3, param4, param5):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.param4 = param5
        self.param5 = param5
        #Размеры головы
        self.head_w = self.param1 * py5.random(30, 50) 
        self.head_h = self.param1 * py5.random(40, 50)
        #Размеры тела
        self.body = (self.head_w + self.head_h) * self.param2
        #Размеры брюшка
        self.abdomen_w = (self.body + self.head_h) / self.param3
        self.abdomen_h = (self.abdomen_w * 4) / self.param3
        #Координаты начала лап
        self.legs1_y = 5 + py5.random(0, 5 + self.param4) 
        self.legs2_y = 10 + py5.random(0, 5 + self.param4) 
        self.legs3_y = 15 + py5.random(0, 5 + self.param4) 
        #Длина лап
        self.legs1_l = py5.random(30, 30 + self.param5) 
        self.legs2_l = py5.random(40, 40 + self.param5) 
        self.legs3_l = py5.random(20, 20 + self.param5) 
        #Число изломов в лапах
        self.legs1_n = 4
        self.legs2_n = 3
        self.legs3_n = 3
        #Угол излома лап
        self.legs1_angle = -40
        self.legs2_angle = -30
        self.legs3_angle = -10
         
    def show(self, x, y):
        py5.push_matrix()
        py5.stroke(0)
        py5.fill(0)
        #Переходим в точку отрисовки
        py5.translate(x,y)
        py5.rect_mode(py5.CENTER)
        #Отрисовка головы
        py5.rect(0, 0, self.head_w, self.head_h,
                 self.param1 * (self.head_h - self.body), 
                 self.param1 * (self.head_h - self.body),
                 20,
                 20)
        #Отрисовка тела
        py5.circle(0, self.head_h/2 + self.body/2, self.body)
        #Отрисовка брюшка
        py5.ellipse(0, self.head_h/2 + self.body + self.abdomen_h/2, self.abdomen_w, self.abdomen_h)
        #Отрисовка лап
        leg_recursion(0, self.head_h + self.legs1_y, self.legs1_l, self.legs1_n, self.legs1_angle)
        #left_leg_recursion(0, self.head_h + self.legs1_y, self.legs1_l, self.legs1_n, 180 - self.legs1_angle)
        leg_recursion(0, self.head_h + self.legs2_y, self.legs2_l, self.legs2_n, self.legs2_angle)
        #leg_recursion(0, self.head_h + self.legs2_y, self.legs2_l, self.legs2_n, 180 - self.legs2_angle)
        leg_recursion(0, self.head_h + self.legs3_y, self.legs3_l, self.legs3_n, self.legs3_angle)
        #leg_recursion(0, self.head_h + self.legs2_y, self.legs2_l, self.legs2_n, 180 - self.legs2_angle)
        
        
        py5.pop_matrix()


"""
Функция отрисовки лапы (рекурсивная)

x -
y - 
length - 
fracture_num -
"""
def leg_recursion(x, y, length, fracture_num, angle):
    if fracture_num == 0:
        return
    py5.push_matrix()
    py5.translate(x, y)
    py5.rotate(py5.radians(angle))
    py5.line(0, 0, length, 0)
    leg_recursion(length, 0, length/2, fracture_num - 1, angle)
    py5.pop_matrix()

"""
def left_leg_recursion(x, y, length, fracture_num, angle):
    if fracture_num == 0:
        return
    py5.push_matrix()
    py5.translate(x, y)
    py5.rotate(py5.radians(angle))
    py5.line(0, 0, length, 0)
    left_leg_recursion(length, 0, length/2, fracture_num - 1, -180 + angle)
    py5.pop_matrix()
"""
        
    
    
    