# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:16:56 2023

@author: Evgeniy
"""

import py5

"""
Класс Rule

Служит для хранения правил L-системы

a - то что было

b - на что меняем

"""

class Rule:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getA(self):
        return self.a

    def getB(self):
        return self.b