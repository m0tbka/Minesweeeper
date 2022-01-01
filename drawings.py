import pygame
from board import Board


def draw_board(board: Board, surface: pygame.Surface):
    for i in range(board.height):
        for j in range(board.width):
            pygame.draw.rect(surface, board.color_pole, (
                board.left + j * board.cell_size, board.top + i * board.cell_size, board.cell_size,
                board.cell_size), 2)


def update_board(board: Board, surface: pygame.Surface):
    for i in range(board.height):
        for j in range(board.width):
            if board.visible[i][j] == 1 and board.need_update[i][j] == 1:
                if board.board[i][j] == -1:
                    pygame.draw.rect(surface, board.color_mine, (
                        board.left + j * board.cell_size + 1, board.top + i * board.cell_size + 1, board.cell_size - 1,
                        board.cell_size - 1))
                if board.board[i][j] > 0:
                    draw_rim_number(board, surface, board.board[i][j], board.left + j * board.cell_size,
                                    board.top + i * board.cell_size, board.cell_size)
                board.need_update[i][j] = 0
    return board


def draw_rim_number(board: Board, surface: pygame.Surface, number, x, y, cell_size):
    if number == 1:
        pygame.draw.line(surface, board.color_number,
                         (x + cell_size // 2, y + cell_size // 10), (x + cell_size // 2, y + cell_size // 10 * 9), 2)
    if number == 2:
        pygame.draw.line(surface, board.color_pole, (x + cell_size // 3, y + cell_size // 10),
                         (x + cell_size // 3, y + cell_size // 10 * 9), 2)
        pygame.draw.line(surface, board.color_pole, (x + cell_size // 3 * 2, y + cell_size // 10),
                         (x + cell_size // 3 * 2, y + cell_size // 10 * 9), 2)
