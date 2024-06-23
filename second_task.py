"""Реализация игры сапёр на классах."""
from typing import Any

import random


class Cell():
    """Классс представления игрового поля."""

    def __init__(self, around_mines: int, mine: bool) -> None:
        """."""
        self.around_mines: int = around_mines
        self.mine: bool = mine
        self.fl_open: bool = False


class GamePole():
    """Класс для управления игровым полем."""

    def __init__(self, N: int, M: int) -> None:
        """."""
        self.N: int = N
        self.M: int = M
        self.pole: list[list[Any]] = (
            [
                [Cell(0, False) for _ in range(N)]
                for _ in range(N)
            ]
        )
        self.init()

    def _around(self, x: int, y: int) -> None:
        """Подсчёт мин вокруг не мины."""
        for i in range(max(0, x-1), min(x+2, self.N)):
            for j in range(max(0, y-1), min(y+2, self.N)):
                if not self.pole[i][j].mine:
                    self.pole[i][j].around_mines += 1

    def init(self) -> None:
        """Инициализация поля с расстановкой M мин."""
        mine_count = self.M
        while mine_count > 0:
            x = random.randint(0, self.N-1)
            y = random.randint(0, self.N-1)
            if not self.pole[x][y].mine:
                self.pole[x][y].mine = True
                mine_count -= 1
                self._around(x, y)

    def show(self) -> None:
        """Отображение игрового поля в консоли."""
        for i in range(self.N):
            for j in range(self.N):
                if not self.pole[i][j].fl_open:
                    print('#', end=' ')
                elif self.pole[i][j].mine:
                    print('*', end=' ')
                else:
                    print(self.pole[i][j].around_mines, end=' ')
            print(end='\n')


if __name__ == '__main__':
    pole_game = GamePole(10, 12)
    pole_game.show()
