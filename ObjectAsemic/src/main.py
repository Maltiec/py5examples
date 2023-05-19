# -*- coding: utf-8 -*-
"""
Created on Fri May 19 16:39:48 2023

@author: Evgeniy
"""

import py5
from my_symbol import Symbol
from my_key import Key

def setup():
    py5.size(500, 500)
    py5.background(0)
    py5.stroke(255)
    py5.fill(255)
    symbols = []
    keys = []
    """
    for i in range(20):
        symbols.append(Symbol(0, 0))
    
    for i in range(len(symbols)):
        symbols[i].show(50 * i,250)
    """
    #test_symbol = Symbol(0, 0)
    #test_symbol.show(250, 250)
    for i in range(10):
        keys.append(Key(0, 0, 0))
    
    for i in range(len(keys)):
        py5.push_matrix()
        py5.translate(40 * i + 20, 250)
        keys[i].show()
        py5.pop_matrix()
    #test_key = Key(0, 0, 0)
    #test_key.show()
    
py5.run_sketch()