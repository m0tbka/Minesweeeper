import pygame
from minesweaper import Minesweaper
import drawings


def main():
    game = Minesweaper(900, 700, 35, 150)
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
