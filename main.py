import pygame
from minesweaper import Minesw
import drawings


def main():
    game = Minesw(900, 700, 35)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()


if __name__ == '__main__':
    main()
