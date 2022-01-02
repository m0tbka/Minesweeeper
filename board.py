import pygame


class Board:
    COLOURS = [(100, 100, 100), "blue", "green", "red", (100, 100, 180), (180, 100, 100), (100, 180, 100),
               (180, 180, 180)]

    def __init__(self, width, height, cell_size, color_pole, color_mine, color_flag):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.visible = [[0] * width for _ in range(height)]
        self.need_update = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = cell_size
        self.color_pole = color_pole
        self.color_mine = color_mine
        self.color_flag = color_flag

    """Возвращает индексы клетки по заданным координатам с поля"""

    def get_cell(self, coordinates):
        return (coordinates[1] - self.left) // self.cell_size, (coordinates[0] - self.top) // self.cell_size
