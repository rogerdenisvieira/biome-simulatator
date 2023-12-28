import pygame
import random

from enum import Enum
from pygame.surface import Surface


class Subject:

    def draw(self, window: Surface):

        pygame.draw.circle(
            surface=window, 
            color=self._color, 
            center=(self._x, self._y), 
            radius=self._size
        )

    def random_move(self, window: Surface):
        self._x += random.randint(-self._speed,self._speed)
        self._y += random.randint(-self._speed,self._speed)
        self.draw(window)
    
    def move(self, direction: Enum, window: Surface):
        self._x += direction.value[0] * self._speed
        self._y += direction.value[1] * self._speed
        
        print("drawing...")
        self.draw(window)



    def __init__(self, size: int, health: int, speed: int, window: Surface):
        self._size = size
        self._color = (random.randint(100,255), random.randint(100,255), random.randint(100,255))
        self._health = health
        self._speed = speed
        self._x = random.randint(0, window.get_width())
        self._y = random.randint(0, window.get_height())

        self.draw(window)


class Direction(Enum):
    UP = (1,0)
    RIGHT = (0,1)
    DOWN = (-1,0)
    LEFT = (0,-1)