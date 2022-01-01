import pygame
from board import Board
import drawings
from random import randrange as randint


class Minesw:
    def __init__(self, width, height, cell_size):
        self.screen = pygame.display.set_mode((width, height))
        self.board = Board((width - 20) // cell_size, (height - 20) // cell_size, cell_size, "white", "red", "green")
        self.amount_mines = 0
        self.set_mines(10)
        drawings.draw_board(self.board, self.screen)

    def set_mines(self, amount):
        self.amount_mines = amount
        for _ in range(amount):
            self.board.board[randint(0, self.board.height)][randint(0, self.board.width)] = -1

