# -*- coding: utf-8 -*-
"""
Created on Fri May 19 16:40:20 2023

@author: Evgeniy
"""

class Alphabet:
    def __init__(self, symbols_num):
        self.symbols_num = symbols_num
        self.symbols_cont = []
    
    def add_symbol(self, symbol):
        self.symbols_cont.append(symbol)
    
    def get_symbol(self, symbol_index):
        symbol = self.symbols_cont[symbol_index]
        return symbol
    
    def shuffle_symbols(self):
        pass