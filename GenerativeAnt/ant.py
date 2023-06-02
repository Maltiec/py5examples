# -*- coding: utf-8 -*-

import py5

class Ant:
    def __init__(self, head_param, body_param, abdomen_param, legs_len_param):
        self.head_param = head_param
        self.body_param = body_param
        self.abdomen_param = abdomen_param
        self.legs_len_param = legs_len_param
        #Размеры головы
        self.head_h = py5.remap(head_param, 0, 1, 10, 40)
        self.head_w = py5.remap(head_param, 0, 1, 20, 30)
        #self.head_w = self.param1 * py5.random(30, 50) 
        #self.head_h = self.param1 * py5.random(40, 50)
        #Размеры тела
        self.body = py5.remap(body_param, 0, 1, (self.head_w + self.head_h) / 4, (self.head_w + self.head_h) / 2) 
        #self.body = (self.head_w + self.head_h) * self.param2
        #Размеры брюшка
        self.abdomen_w = py5.remap(self.abdomen_param, 0, 1, (self.body + self.head_h)/3, (self.body + self.head_h))
        #self.abdomen_w = (self.body + self.head_h) / self.param3
        self.abdomen_h = py5.remap(self.abdomen_param, 0, 1, self.abdomen_w * 1.5, self.abdomen_w * 2)
        #Координаты начала лап
        self.legs1_y = 5
        self.legs2_y = 10
        self.legs3_y = 15
        #Длина лап
        self.legs1_l = py5.remap(self.legs_len_param, 0, 1, 15, 20)
        self.legs2_l = py5.remap(self.legs_len_param, 0, 1, 25, 40)
        self.legs3_l = py5.remap(self.legs_len_param, 0, 1, 30, 45)
        #Число изломов в лапах
        self.legs1_n = int(py5.remap(self.legs1_l, 15, 20, 2, 5))
        self.legs2_n = int(py5.remap(self.legs2_l, 25, 40, 1, 3))
        self.legs3_n = int(py5.remap(self.legs3_l, 30, 45, 2, 5))
        #Угол излома лап
        self.legs1_angle = -(py5.remap(self.legs1_l, 15, 20, 30, 50))
        self.legs2_angle = -(py5.remap(self.legs2_l, 25, 40, 30, 40))
        self.legs3_angle = -(py5.remap(self.legs3_l, 30, 45, 10, 30))
        #self.legs1_angle = -30 + py5.random_int(-20, -10)
        #self.legs2_angle = -30 + py5.random_int(-10, -5)
        #self.legs3_angle = -10 + py5.random_int(-10, -5)
         
    def show(self, x, y):
        py5.push_matrix()
        py5.stroke(0)
        py5.fill(0)
        #Переходим в точку отрисовки
        py5.translate(x,y)
        py5.rect_mode(py5.CENTER)
        #Отрисовка головы
        py5.rect(0, 0, self.head_w, self.head_h,
                 self.head_param * abs(self.head_h - self.body), 
                 self.head_param * abs(self.head_h - self.body),
                 20,
                 20)
        #Отрисовка тела
        py5.circle(0, self.head_h/2 + self.body/2, self.body)
        #Отрисовка брюшка
        py5.ellipse(0, self.head_h/2 + self.body + self.abdomen_h/2, self.abdomen_w, self.abdomen_h)
        #Отрисовка лап
        leg_recursion(0, self.head_h + self.legs1_y, self.legs1_l, self.legs1_n, self.legs1_angle)
        left_leg_recursion(0, self.head_h + self.legs1_y, self.legs1_l, self.legs1_n, -self.legs1_angle)
        leg_recursion(0, self.head_h + self.legs2_y, self.legs2_l, self.legs2_n, self.legs2_angle)
        left_leg_recursion(0, self.head_h + self.legs2_y, self.legs2_l, self.legs2_n, - self.legs2_angle)
        leg_recursion(0, self.head_h + self.legs3_y, self.legs3_l, self.legs3_n, self.legs3_angle)
        left_leg_recursion(0, self.head_h + self.legs3_y, self.legs3_l, self.legs3_n, - self.legs3_angle)
        
        
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


def left_leg_recursion(x, y, length, fracture_num, angle):
    if fracture_num == 0:
        return
    py5.push_matrix()
    py5.translate(x, y)
    py5.rotate(py5.radians(angle))
    py5.line(0, 0, -length, 0)
    left_leg_recursion(-length, 0, length/2, fracture_num - 1, angle)
    py5.pop_matrix()

        
    
    
    