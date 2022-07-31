import pygame
from time import time

import board
from board import Board
import drawings
from random import randrange as randint


class Minesweeper:
    def __init__(self, width, height, amount_mines=10, cell_size=35):
        self.condition = 0
        self.width = width * cell_size + 20
        self.height = height * cell_size + 20
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.board = Board(width, height, cell_size, "white", "red", "purple")
        self.amount_mines = amount_mines
        drawings.draw_board(self.board, self.screen)
        self.set_mines(self.amount_mines)
        self.beginning_time = time()
        self.ending_time = time()

    def begin_new_game(self):
        self.clear()
        self.set_mines(self.amount_mines)
        self.beginning_time = time()

    def am_i_winning(self):
        if self.condition != 0:
            return
        flag = 0
        correct_flag = 0
        for i in range(self.board.height):
            for j in range(self.board.width):
                if self.board.visible[i][j] == -2:
                    if self.board.board[i][j] == -1:
                        correct_flag += 1
                    else:
                        flag += 1
                    # print(i, j)
        if correct_flag == self.amount_mines and flag == 0:
            self.condition = 1
            self.show()
            self.board = drawings.update_board(self.board, self.screen)
        # print(flag)
        self.ending_time = time()

    def defeat(self):
        self.condition = -1
        self.show(0)
        self.board = drawings.update_board(self.board, self.screen)

    def clear(self):
        self.condition = 0
        self.board = Board(self.board.width, self.board.height, self.board.cell_size, "white", "red", "purple")
        drawings.draw_board(self.board, self.screen)

    def set_mines(self, amount):
        self.amount_mines = amount
        for _ in range(amount):
            i, j = randint(0, self.board.height), randint(0, self.board.width)
            self.board.board[i][j] = -1
            # self.board.visible[i][j] = 1
            self.board.need_update[i][j] = 1
        self.amount_mines = 0
        for i in range(self.board.height):
            for j in range(self.board.width):
                if self.board.board[i][j] == -1:
                    self.amount_mines += 1
        print(f"Actual amount of mines: {self.amount_mines}")
        self.set_numbers()

    def set_numbers(self):
        for i in range(self.board.height):
            for j in range(self.board.width):
                if self.board.board[i][j] != -1:
                    nearer_mines = 0
                    for iq in range(-1, 2):
                        for jq in range(-1, 2):
                            if 0 <= i + iq < self.board.height and 0 <= j + jq < self.board.width:
                                if self.board.board[i + iq][j + jq] == -1:
                                    nearer_mines += 1
                    self.board.board[i][j] = nearer_mines

    def clicker(self, event):
        indexes = self.board.get_cell(event.pos)
        if indexes[0] >= self.board.height or indexes[1] >= self.board.width:
            return None
        if event.button == 1:
            if self.board.visible[indexes[0]][indexes[1]] == 0:
                if self.board.board[indexes[0]][indexes[1]] == -1:
                    self.defeat()
                    # self.board.visible[indexes[0]][indexes[1]] = 1
                    # self.board.need_update[indexes[0]][indexes[1]] = 1
                else:
                    self.dfs(indexes[0], indexes[1])
        if event.button == 3:
            if self.board.visible[indexes[0]][indexes[1]] == 0:
                self.board.visible[indexes[0]][indexes[1]] = -2
                self.board.need_update[indexes[0]][indexes[1]] = 1
            elif self.board.visible[indexes[0]][indexes[1]] == -2:
                self.board.visible[indexes[0]][indexes[1]] = 0
                self.board.need_update[indexes[0]][indexes[1]] = 1

    def dfs(self, i, j):
        if not 0 <= i < self.height or not 0 <= j < self.width or self.board.board[i][j] == -1 or \
                self.board.need_update[i][j] == 1 or self.board.visible[i][j] == -2:
            return
        self.board.need_update[i][j] = 1
        self.board.visible[i][j] = 1
        if self.board.board[i][j] > 0:
            return
        for iq in range(-1, 2):
            for jq in range(-1, 2):
                if 0 <= i + iq < self.board.height and 0 <= j + jq < self.board.width:
                    self.dfs(i + iq, j + jq)

    def show(self, what_to_show=1):
        for i in range(self.board.height):
            for j in range(self.board.width):
                if (what_to_show and self.board.visible[i][j] != -2) or not what_to_show:
                    self.board.visible[i][j] = 1
                    self.board.need_update[i][j] = 1

    def drawer(self):
        self.am_i_winning()
        if self.condition != 0:
            if self.condition == -1:
                text = "BOOM"
                font = self.board.width * self.board.cell_size // 4
                k = 10 / 3
            else:
                text = f"Defused in {min(int(self.ending_time - self.beginning_time), 999)} s"
                font = self.board.width * self.board.cell_size // 8
                k = 5
            drawings.draw_boom(self.screen, self.board, text, font, k)
        else:
            self.board = drawings.update_board(self.board, self.screen)
