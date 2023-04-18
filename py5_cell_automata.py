#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 09:50:53 2023

@author: evgeniy
"""

import py5
import random
import time


def setup():
    global test_cell, board
    py5.size(800, 800)
    py5.background(128)
    board = []
    # Создание "доски" для клеток
    for i in range(50):
        row = []
        board.append(row)
        for j in range(50):
            board[i].append(
                Cell(
                    15 + i * 15,
                    15 + j * 15,
                    random.randint(0, 1),
                ),
            )


def draw():
    py5.background(128)
    # Вычисление новых состояний клеток
    for x in range(0, len(board) - 1):
        for y in range(0, len(board[x]) - 1):
            neighbours_alive = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if board[x + i][y + j].previous_state > 0:
                        neighbours_alive += 1
            if board[x][y].previous_state == 1:
                neighbours_alive -= 1
            # Если число соседей равно 3 и клетка была раньше мертва
            if neighbours_alive == 3 and board[x][y].previous_state == 0:
                board[x][y].cell_newstate(1)
            # Если число соседей больше 2
            elif (
                neighbours_alive > 2
                and neighbours_alive < 5
                and board[x][y].previous_state == 1
            ):
                board[x][y].cell_newstate(1)
            # В любом ином случае клетка умирает
            else:
                board[x][y].cell_newstate(0)
    # Отрисовка доски с клетками
    for i in range(50):
        for j in range(50):
            board[i][j].cell_show()
    # Задержка
    time.sleep(0.1)


py5.run_sketch()


class Cell:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.previous_state = self.state
        self.size = 10

    def cell_show(self):
        # Оценка состояния клетки и выбор цвета отрисовки
        if self.previous_state == 1 and self.state == 0:
            color = py5.color(255, 0, 0)
        elif self.previous_state == 1 and self.state == 1:
            color = py5.color(0, 0, 0)
        elif self.previous_state == 0 and self.state == 1:
            color = py5.color(0, 255, 0)
        elif self.previous_state == 0 and self.state == 0:
            color = py5.color(255, 255, 255)
        # Перемещение экранной матрицы и отрисовка клетки
        py5.remap(self.state, 0, 1, 255, 0)
        py5.stroke(color)
        py5.fill(color)
        py5.push_matrix()
        py5.translate(self.x, self.y)
        py5.rect_mode(py5.CORNER)
        py5.square(0, 0, self.size)
        py5.pop_matrix()

    def cell_newstate(self, new_state):
        self.previous_state = self.state
        self.state = new_state
