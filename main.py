import array
import random
import sys
from typing import List
import pygame
import logging
from pygame.surface import Surface
from field import Field
from subject import Subject, Direction
from specimen import Specimen

WIDTH, HEIGHT = 1280, 960
FPS = 30


class Game:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption("Biome Simulator")
        self.window = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self.subjects: List[Subject] = []

        for i in range(0, 50):
            self.subjects.append(Subject(f"Subject {i}", 10, 1000, random.randint(1,5), self.window))

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for s in self.subjects:
                s.random_move(self.window)
                s.detect_collision(self.subjects)

            pygame.display.update()

            self.window.fill((0, 64, 0))
            self.clock.tick(FPS)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("starting...")
    game = Game()
    game.run()
