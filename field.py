from pygame import Surface
import pygame
import logging


class Field:
    def __init__(self, window: Surface) -> None:
        self.window = window

    def run(self) -> None:
        for x in range(self.window.get_width()):
            for y in range(self.window.get_height()):
                if x % 10 == 0 | y % 10 == 0:
                    pygame.draw.circle(
                        self.window,
                        color=(255, 0, 0),
                        center=(x + 10, y + 10),
                        radius=10,
                    )
                    logging.info(f"Coordinate: [({x+10},{y+10})]")
                    pygame.display.update()
