import logging
from typing import Tuple
from pygame import Surface
import pygame

X_OFFSET = 14
Y_OFFSET = 25
WIDTH = 28
HEIGHT = 7


class HealthBar:
    def __init__(self, health: int, pos: Tuple[int, int], window: Surface) -> None:
        self._window = window
        self.__max_health = health
        self.__health = health
        self._x = pos[0]
        self._y = pos[1]

    def draw(self, pos: Tuple[int, int]) -> None:
        self._x = pos[0]
        self._y = pos[1]

        internal_width = (self.__health * 24)/self.__max_health

        # external rect
        pygame.draw.rect(
            self._window,
            (0, 0, 0),
            (self._x - X_OFFSET, self._y - Y_OFFSET, WIDTH, HEIGHT),
        )

        # internal rect
        pygame.draw.rect(
            self._window,
            (0, 255, 0),
            (self._x - X_OFFSET +2, self._y - Y_OFFSET + 2, internal_width, 3),
        )


        logging.info(f'ratio: {internal_width}')

    def decrease(self):
        if self.__health > 0:
            self.__health -= 1

    def get_health(self) -> int:
        return self.__health
