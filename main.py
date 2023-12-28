import pygame
import logging
import random
from pygame.surface import Surface
from planet import Planet
from subject import Subject, Direction
from specimen import Specimen

pygame.init()




WIDTH, HEIGHT = 800, 800

RED = (255,0,0)
BLACK = (0,0,0)




def game_loop(window: Surface):
    run = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(0)
   

    subject = Specimen(1000, 1,10,10)
    subject.rect.x = 400
    subject.rect.y = 400

    all_sprites_list = pygame.sprite.Group() 
    all_sprites_list.add(subject)


    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # -------------------- GAME LOOP -------------------- 

        subject.rect.x =  pygame.mouse.get_pos()[0]
        subject.rect.y = pygame.mouse.get_pos()[1]

        print(pygame.mouse.get_pos()[0])
        
        
        
        all_sprites_list.update()
        window.fill(BLACK)

        all_sprites_list.draw(window)




        # --------------------------------------------------- 

        pygame.display.update()
        
        
    pygame.quit()



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.debug('starting...')

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    game_loop(window)
