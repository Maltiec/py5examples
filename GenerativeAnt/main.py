# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:35:19 2023

@author: Evgeniy
"""

import py5
from ant import Ant

def setup():
    global test_ant, ants, ants2, ants3, ants4
    py5.size(1100, 700)
    py5.background(255)
    #test_ant = Ant(py5.random(0.1, 0.8), py5.random(0.8, 0.9), 2.1, py5.random(5,7), 20)
    ants = []
    ants2 = []
    ants3 = []
    ants4 = []
    head_param = 0.0
    body_param = 0.0
    abdomen_param = 0.0
    legs_len_param = 0.0
    
    for i in range(100):
        ants.append(Ant(py5.random(0,1), py5.random(0, 1), py5.random(0, 1), py5.random(0, 1)))
    """
    for i in range(10):
        ants2.append(Ant(0.5, body_param, 0.5, 0.5))
        body_param += 0.1
    for i in range(10):
        ants3.append(Ant(0.5, 0.5, abdomen_param, 0.5))
        abdomen_param += 0.1
    for i in range(10):
        ants4.append(Ant(0.5, 0.5, 0.5, legs_len_param))
        legs_len_param += 0.1
    """
    
def draw():
    global test_ant, ants, ants2, ants3, ants4
    index1 = py5.random_int(0, len(ants) - 1)
    index2 = py5.random_int(0, len(ants) - 1)
    ant1 = ants[index1]
    ant2 = ants[index2]
    ant1.show(100, 500)
    ant2.show(200, 500)
    head_gene = [ant1.head_param, ant2.head_param]
    body_gene = [ant1.body_param, ant2.body_param]
    abdomen_gene = [ant1.abdomen_param, ant2.abdomen_param]
    legs_len_gene = [ant1.legs_len_param, ant2.legs_len_param]
    random_value = py5.random()
    if random_value > 0.5:
        ant3_head_gene = head_gene[0]
    else:
        ant3_head_gene = head_gene[1]
    random_value = py5.random()
    if random_value > 0.5:
        ant3_body_gene = body_gene[0]
    else:
        ant3_body_gene = body_gene[1]
    random_value = py5.random()
    if random_value > 0.5:
        ant3_abdomen_gene = abdomen_gene[0]
    else:
        ant3_abdomen_gene = abdomen_gene[1]
    random_value = py5.random()
    if random_value > 0.5:
        ant3_legs_len_gene = legs_len_gene[0]
    else:
        ant3_legs_len_gene =legs_len_gene[1]
    
    ant3 = Ant(ant3_head_gene, ant3_body_gene, ant3_abdomen_gene, ant3_legs_len_gene)
    ant3.show(150, 400)
    """
    for i in range(len(ants2)):
        ants2[i].show(100 + 100 * i, 250)
    for i in range(len(ants3)):
        ants3[i].show(100 + 100 * i, 350)
    for i in range(len(ants4)):
        ants4[i].show(100 + 100 * i, 500)
    """
    #test_ant.show(250, 250)
    py5.no_loop()
py5.run_sketch()