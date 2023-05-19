# -*- coding: utf-8 -*-
"""
Created on Fri May 19 16:40:07 2023

@author: Evgeniy
"""

import py5

"""
Коды структур:
         N
  1: N N N
         N
  2: N
     N
     N
  
  3: N N N
  
       N   
  4: N   N
  
  5: N N
  
  6: N
     N

  7: N
"""

class Symbol:
    
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        self.keys_list = []
        self.structure = 0
        self.keys_count = py5.random_int(1,3)
        self.keys_dict = ['0', '1', '2', '3', '4','5', '6', '7', '8', '9']
        if self.keys_count == 1:
            temp_random = py5.random()
            if temp_random < 0.5:
                self.structure = 4
            elif temp_random >= 0.5:
                self.structure = 7
        if self.keys_count == 2:
            temp_random = py5.random()
            if temp_random < 0.5:
                self.structure = 5
            elif temp_random >= 0.5:
                self.structure = 6
        if self.keys_count == 3:
            temp_random = py5.random()
            if temp_random <= 0.3:
                self.structure = 1
            elif temp_random > 0.3 and temp_random <= 0.6:
                self.structure = 2
            elif temp_random > 0.6:
                self.structure = 3
        for i in range(self.keys_count):
            random_index = py5.random_int(0, len(self.keys_dict) - 1)
            self.keys_list.append(self.keys_dict[random_index])
        
    def show(self, x, y):
        if self.structure == 1:
            py5.push_matrix()
            py5.translate(x, y)
            py5.text(self.keys_list[0], 0, 0)
            py5.text(self.keys_list[1], 10, 0)
            py5.text(self.keys_list[2], 20, 0)
            py5.text(self.keys_list[0], 20, 10)
            py5.text(self.keys_list[1], 20, -10)
            py5.pop_matrix()
        elif self.structure == 2:
            py5.push_matrix()
            py5.translate(x, y)
            py5.text(self.keys_list[0], 0, 0)
            py5.text(self.keys_list[1], 0, -10)
            py5.text(self.keys_list[2], 0, 10)
            py5.pop_matrix()
        elif self.structure == 3:
            py5.push_matrix()
            py5.translate(x, y)
            py5.text(self.keys_list[0], 0, 0)
            py5.text(self.keys_list[1], 10, 0)
            py5.text(self.keys_list[2], 20, 0)
            py5.pop_matrix()
        elif self.structure == 4:
            py5.push_matrix()
            py5.translate(x, y)
            py5.text(self.keys_list[0], 0, 0)
            py5.text(self.keys_list[0], 10, 0)
            py5.text(self.keys_list[0], 5, 10)
            py5.pop_matrix()
        elif self.structure == 5:
            py5.push_matrix()
            py5.translate(x, y)
            py5.text(self.keys_list[0], 0, 0)
            py5.text(self.keys_list[1], 10, 0)
            py5.pop_matrix()
        elif self.structure == 6:
            py5.push_matrix()
            py5.translate(x, y)
            py5.text(self.keys_list[0], 0, 0)
            py5.text(self.keys_list[1], 0, -10)
            py5.pop_matrix()
        elif self.structure == 7:
            py5.push_matrix()
            py5.translate(x, y)
            py5.text(self.keys_list[0], 0, 0)
            py5.pop_matrix()
        elif self.structure == 0:
            print('Ошибка! Структура не выбрана')