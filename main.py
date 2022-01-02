import pygame
from minesweaper import Minesweaper
import drawings


def main():
    # Minesweaper(кол-во клеток по горизонтали, кол-во клеток по вертикали, кол-во мин, размер одной клетки)
    game = Minesweaper(20, 20, 70, 35)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.clicker(event)
        game.board = drawings.update_board(game.board, game.screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
