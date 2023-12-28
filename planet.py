import pygame
from pygame.surface import Surface


class Planet:

    def __init__(self, radius, color, mass):
        self._radius = radius
        self._color = color
        self._mass = mass

    def draw(self, x, y, window: Surface):

        pygame.draw.circle(
            surface=window, 
            color=self._color, 
            center=(x, y), 
            radius=self._radius
        )



