import pygame, random
from enum import Enum

class Specimen(pygame.sprite.Sprite):

    def __init__(self, health: int, speed: int, height: int, width: int):
        super().__init__()

        
        self._color = (random.randint(100,255), random.randint(100,255), random.randint(100,255))
        self._health = health
        self._speed = speed

        self.image = pygame.Surface([width,height])
        # self.image.fill((0,255,0))
        # self.image.set_colorkey((255,0,0))

        pygame.draw.rect(self.image, self._color, pygame.Rect(0,0,width, height))

        self.rect = self.image.get_rect()
    

class Direction(Enum):
    UP = (1,0)
    RIGHT = (0,1)
    DOWN = (-1,0)
    LEFT = (0,-1)