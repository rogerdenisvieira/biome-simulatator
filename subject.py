import logging
import random, pygame
from typing import List
from enum import Enum
from pygame import Surface, Rect
from bar import Bar
from utils import random_color


class Subject:
    def __init__(
        self, name: str, radius: int, health: int, speed: int, window: Surface
    ):
        self.__name = name
        self.__size = random.randint(10, 25)
        self.__window = window
        self.__health = health
        self.__speed = speed
        self.__x = random.randint(0, window.get_width())
        self.__y = random.randint(0, window.get_height())
        self.__original_color = self.__color = random_color()
        self.__healthbar = Bar(self.__health, (self.__x, self.__y), self.__window)
        self.draw(window)

    def draw(self, window: Surface) -> None:
        self.__healthbar.draw((self.__x, self.__y - self.__size))

        self.__collision = pygame.draw.circle(
            surface=window,
            color=self.__color,
            center=(self.__x, self.__y),
            radius=self.__size,
        )

        pygame.draw.rect(self.__window, (0, 0, 0), self.__collision, -1)

    def random_move(self, window: Surface) -> None:
        self.__x += random.randint(-self.__speed, self.__speed)
        self.__y += random.randint(-self.__speed, self.__speed)
        self.draw(window)

    # def move(self, direction: Enum, window: Surface) -> None:
    #     self.__x += direction.value[0] * self.__speed
    #     self.__y += direction.value[1] * self.__speed

    #     print("drawing...")
    #     self.draw(window)

    def get_collision(self) -> Rect:
        return self.__collision

    def take_damage(self, damage: int) -> None:
        if self.__health > 0:
            self.__health -= damage
        else:
            self.__health = 0
            self.__speed = 0

        self.__color = (255, 0, 0)
        self.__healthbar.set_value(damage)

    def collided(self, subjects):
        for s in subjects:
            self.__color = self.__original_color

            was_collided = pygame.Rect.colliderect(
                self.get_collision(), s.get_collision()
            )

            if was_collided and s.__name != self.__name:
                logging.info(f"[ {self.__name} ] collided to [ {s.__name} ]")
                self.take_damage(10)



class Direction(Enum):
    UP = (1, 0)
    RIGHT = (0, 1)
    DOWN = (-1, 0)
    LEFT = (0, -1)
