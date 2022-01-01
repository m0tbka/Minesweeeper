import pygame
from board import Board


def draw_board(board: Board, surface: pygame.Surface):
    for i in range(board.height):
        for j in range(board.width):
            if board.visible[i][j] == 1:
                if board.board[i][j] == -1:
                    pygame.draw.rect(surface, board.color_mine, (
                        board.left + j * board.cell_size, board.top + i * board.cell_size, board.cell_size,
                        board.cell_size))
                if board.board[i][j] == 0:
                    pygame.draw.rect(surface, board.color_pole, (
                        board.left + j * board.cell_size, board.top + i * board.cell_size, board.cell_size,
                        board.cell_size), 1)
                else:
                    pygame.draw.rect(surface, board.color_pole, (
                        board.left + j * board.cell_size, board.top + i * board.cell_size, board.cell_size,
                        board.cell_size), 1)
                    # +нарисовать цифру
