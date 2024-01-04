import logging
from typing import Tuple
from pygame import Surface
import pygame

Y_OFFSET = 20
INT_WIDTH = 26
INT_HEIGHT = 4
EXT_WIDTH = 30
EXT_HEIGHT = 8


class Bar:
    def __init__(self, max_value: int, pos: Tuple[int, int], window: Surface) -> None:
        self._window = window
        self.__max_value = max_value
        self.__value = max_value
        self._x = pos[0]
        self._y = pos[1]

    def draw(self, pos: Tuple[int, int]) -> None:
        self._x = pos[0]
        self._y = pos[1]

        current_int_width = (self.__value * INT_WIDTH) / self.__max_value

        # external rect
        pygame.draw.rect(
            self._window,
            (0, 0, 0),
            (
                self._x - EXT_WIDTH / 2,
                self._y - EXT_HEIGHT / 2 - Y_OFFSET,
                EXT_WIDTH,
                EXT_HEIGHT,
            ),
        )

        # internal rect
        pygame.draw.rect(
            self._window,
            (0, 255, 0),
            (
                self._x - EXT_WIDTH / 2 + (EXT_WIDTH - INT_WIDTH) / 2,
                self._y - EXT_HEIGHT / 2 - Y_OFFSET + INT_HEIGHT / 2,
                current_int_width,
                INT_HEIGHT,
            ),
        )

        logging.info(f"ratio: {current_int_width}")

    def set_value(self, value: int):
        if self.__value > 0:
            self.__value -= value

    def get_value(self) -> int:
        return self.__value
