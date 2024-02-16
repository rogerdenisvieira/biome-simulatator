import logging
import random, pygame
from typing import List, Sequence, Self
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

        font = pygame.font.SysFont(None, 24)
        self.__img = font.render(self.__name, True, (255, 255, 255))

        self.draw()

    def draw(self) -> None:
        self.__healthbar.draw((self.__x, self.__y - self.__size))

        self.__collision_box = pygame.draw.circle(
            surface=self.__window,
            color=self.__color,
            center=(self.__x, self.__y),
            radius=self.__size,
        )

        self.update()

        pygame.draw.rect(self.__window, (0, 0, 0), self.__collision_box, -1)
        self.__window.blit(self.__img, (self.__x, self.__y))

    def update(self):
        if self.is_dead():
            self.__color = (0, 0, 0)
        else:
            self.__color = self.__original_color

    def random_move(self, window: Surface) -> None:
        self.__x += random.randint(-self.__speed, self.__speed)
        self.__y += random.randint(-self.__speed, self.__speed)
        self.draw()

    # def move(self, direction: Enum, window: Surface) -> None:
    #     self.__x += direction.value[0] * self.__speed
    #     self.__y += direction.value[1] * self.__speed

    #     print("drawing...")
    #     self.draw(window)

    def is_inbounds(self) -> bool:
        inBounds = pygame.Rect(
            0, 0, self.__window.get_width(), self.__window.get_height()
        ).collidepoint(self.__x, self.__y)
        return inBounds

    def get_collision_box(self) -> Rect:
        return self.__collision_box

    def is_dead(self) -> bool:
        return self.__health <= 0

    def is_alive(self) -> bool:
        return self.__health > 0

    def take_damage(self, damage: int) -> None:
        self.__health -= damage
        self.__healthbar.set_value(self.__health)

        # self.__color = self.__original_color

    def print(self) -> str:
        return f"{self.__name} | H: {self.__health} | S: {self.__speed} | C: [{self.__color}] [{self.__original_color}]"

    def detect_collision(self, subjects: Sequence[Self]):
        # avoid unncessary iterations throught enemies
        if self.is_dead():
            return

        if not self.is_inbounds():
            self.__speed * -1

        self.__color = self.__original_color

        # try using collidepoint from rect

        for subject in subjects:
            was_collided = False

            if self.is_dead():
                self.__speed = 0
                return

            if subject.is_dead() or self is subject:
                continue

            was_collided = pygame.Rect.colliderect(
                self.get_collision_box(), subject.get_collision_box()
            )

            if was_collided:
                logging.info(f"[ {self.print()} ] collided to [ {subject.print()} ]")
                self.__speed * -1
                self.take_damage(10)
                self.__color = (255, 0, 0)


class Direction(Enum):
    UP = (1, 0)
    RIGHT = (0, 1)
    DOWN = (-1, 0)
    LEFT = (0, -1)
