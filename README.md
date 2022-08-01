# Minesweeeper
Simple minesweeper

Instal via archive(only for windows) or all repository.

Then to run game you need to run command:
$ python main.py 'h' 'v' 'm' 'c'
Where 'h' - amount of cells on horizontal axis,
      'v' - amount of cells on vertical axis,
      'm' - amount of mines,
      'c' - size of one cell in the board

Hotkeys:
      'Q' - quit game,
      'R' - restart game,
      'S' - show all cells, include mines and all numbers.
    
 Bugs:
      minesweeper.py -> set_mines: Нет проверки на постановку мины в клетку, где она уже стоит
 
To do:
      1) Пользовательское меню
      2) Таблица лидеров
      3) Персонализация
      4) Помощь игроку
      5) Анимашки
