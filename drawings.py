import pygame
from board import Board


def draw_board(board: Board, surface: pygame.Surface):
    pygame.draw.rect(surface, (0, 0, 0), (
        0, 0, board.height * board.cell_size + board.left,
        board.width * board.cell_size + board.top))
    for i in range(board.height):
        for j in range(board.width):
            pygame.draw.rect(surface, board.color_pole, (
                board.left + j * board.cell_size, board.top + i * board.cell_size, board.cell_size,
                board.cell_size), 2)


def update_board(board: Board, surface: pygame.Surface):
    for i in range(board.height):
        for j in range(board.width):
            if board.need_update[i][j] == 1:
                if board.visible[i][j] == -2:
                    pygame.draw.line(surface, board.color_flag, (
                        board.left + j * board.cell_size + board.cell_size // 4,
                        board.top + i * board.cell_size + board.cell_size // 10), (
                                         board.left + j * board.cell_size + board.cell_size // 4,
                                         board.top + i * board.cell_size + board.cell_size - board.cell_size // 10))
                    # pygame.draw.polygon(surface, board.color_flag, [()])
                if board.visible[i][j] == 1:
                    if board.board[i][j] == -1:
                        pygame.draw.rect(surface, board.color_mine, (
                            board.left + j * board.cell_size + 1, board.top + i * board.cell_size + 1, board.cell_size - 1,
                            board.cell_size - 1))
                    if board.board[i][j] == 0:
                        pygame.draw.rect(surface, board.COLOURS[0], (
                            board.left + j * board.cell_size + 1, board.top + i * board.cell_size + 1, board.cell_size - 1,
                            board.cell_size - 1))
                    if board.board[i][j] > 0:
                        draw_rim_number(board, surface, board.board[i][j], board.left + j * board.cell_size,
                                        board.top + i * board.cell_size, board.cell_size)
                if board.visible[i][j] == 0:
                    print(i, j, 0)
                    pygame.draw.rect(surface, (0, 0, 0), (
                        board.left + j * board.cell_size + 2, board.top + i * board.cell_size + 2, board.cell_size - 4,
                        board.cell_size - 4))
                board.need_update[i][j] = 0
    return board


def draw_rim_number(board: Board, surface: pygame.Surface, number, x, y, cell_size):
    if number == 1:
        pygame.draw.line(surface, board.COLOURS[number],
                         (x + cell_size // 2, y + cell_size // 10),
                         (x + cell_size // 2, y + cell_size - cell_size // 10), 2)
    if number == 2:
        pygame.draw.line(surface, board.COLOURS[number], (x + cell_size // 3, y + cell_size // 10),
                         (x + cell_size // 3, y + cell_size - cell_size // 10), 2)
        pygame.draw.line(surface, board.COLOURS[number], (x + cell_size // 3 * 2, y + cell_size // 10),
                         (x + cell_size // 3 * 2, y + cell_size - cell_size // 10), 2)
    if number == 3:
        for i in range(1, 4):
            pygame.draw.line(surface, board.COLOURS[number], (x + cell_size // 4 * i, y + cell_size // 10),
                             (x + cell_size // 4 * i, y + cell_size - cell_size // 10), 2)
    if number == 4:
        pygame.draw.line(surface, board.COLOURS[number], (x + cell_size // 4, y + cell_size // 10),
                         (x + cell_size // 4, y + cell_size - cell_size // 10), 2)
        pygame.draw.lines(surface, board.COLOURS[number], False, [(x + cell_size // 4 * 2, y + cell_size // 10), (
            x + cell_size // 4 * 2 + cell_size // 8, y + cell_size - cell_size // 10),
                                                                  (x + cell_size // 4 * 3, y + cell_size // 10)], 2)
    if number == 5:
        pygame.draw.lines(surface, board.COLOURS[number], False, [(x + cell_size // 3, y + cell_size // 10), (
            x + cell_size // 2, y + cell_size - cell_size // 10),
                                                                  (x + cell_size // 3 * 2, y + cell_size // 10)], 2)
    if number == 6:
        pygame.draw.line(surface, board.COLOURS[number], (x + cell_size // 4 * 3, y + cell_size // 10),
                         (x + cell_size // 4 * 3, y + cell_size - cell_size // 10), 2)
        pygame.draw.lines(surface, board.COLOURS[number], False, [(x + cell_size // 4, y + cell_size // 10), (
            x + cell_size // 4 + cell_size // 8, y + cell_size - cell_size // 10),
                                                                  (x + cell_size // 4 * 2, y + cell_size // 10)], 2)
    if number == 7:
        pygame.draw.line(surface, board.COLOURS[number], (x + cell_size // 5 * 3, y + cell_size // 10),
                         (x + cell_size // 5 * 3, y + cell_size - cell_size // 10), 2)
        pygame.draw.line(surface, board.COLOURS[number], (x + cell_size // 5 * 4, y + cell_size // 10),
                         (x + cell_size // 5 * 4, y + cell_size - cell_size // 10), 2)
        pygame.draw.lines(surface, board.COLOURS[number], False, [(x + cell_size // 5, y + cell_size // 10), (
            x + cell_size // 5 + cell_size // 10, y + cell_size - cell_size // 10),
                                                                  (x + cell_size // 5 * 2, y + cell_size // 10)], 2)
