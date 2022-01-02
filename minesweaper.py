import pygame
from board import Board
import drawings
from random import randrange as randint


class Minesweaper:
    def __init__(self, width, height, amount_mines=10, cell_size=35):
        self.width = width * cell_size + cell_size * 2
        self.height = height * cell_size + cell_size * 2
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.board = Board(width, height, cell_size, "white", "red", "purple")
        self.amount_mines = amount_mines
        drawings.draw_board(self.board, self.screen)
        self.set_mines(self.amount_mines)

    def clear(self):
        self.board = Board(self.board.width, self.board.height, self.board.cell_size, "white", "red", "purple")

    def set_mines(self, amount):
        self.amount_mines = amount
        for _ in range(amount):
            i, j = randint(0, self.board.height), randint(0, self.board.width)
            self.board.board[i][j] = -1
            # self.board.visible[i][j] = 1
            self.board.need_update[i][j] = 1
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
                    self.board.visible[indexes[0]][indexes[1]] = 1
                    self.board.need_update[indexes[0]][indexes[1]] = 1
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
