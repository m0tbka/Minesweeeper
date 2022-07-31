from sys import argv
import pygame
from minesweeper import Minesweeper
import drawings


def main():
    pygame.init()
    pygame.display.set_caption('Сапер')
    # Minesweeper(кол-во клеток по горизонтали, кол-во клеток по вертикали, кол-во мин, размер одной клетки)
    try:
        width, height, amount_mines, cell_size = map(int, argv[1:])
        assert all((type(width) == int, type(height) == int, type(amount_mines) == int, type(cell_size) == int))
    except AssertionError as error:
        print(f"Wrong args: {error}")
        print("Used standard args: 10 10 9 35")
        width, height, amount_mines, cell_size = 10, 10, 9, 35
    except ValueError as error:
        print(error)
        print("Used standard args: 10 10 9 35")
        width, height, amount_mines, cell_size = 10, 10, 9, 35
    game = Minesweeper(width, height, amount_mines, cell_size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.clicker(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.begin_new_game()
                if event.key == pygame.K_s:
                    game.show()
                if event.key == pygame.K_q:
                    exit(0)
        game.drawer()
        pygame.display.flip()


if __name__ == '__main__':
    main()
