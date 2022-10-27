import pygame
from pygame.locals import *
import time

def draw_thing():
    surface.fill((0, 0, 0))
    surface.blit(block, (blockPos1, blockPos2))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((500, 500))
    surface.fill((0, 0, 0))

    block = pygame.image.load("pog.jpg").convert()
    blockPos1 = 100
    blockPos2 = 500
    surface.blit(block, (blockPos1, blockPos2))

    pog = pygame.image.load("funnyText.jpg").convert()
    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_SPACE:
                    for i in range(266):
                        blockPos2 -= 1
                        draw_thing()
                        time.sleep(.01)
                    surface.blit(pog, (150, 100))
                    pygame.display.flip()
                    time.sleep(5)
                    running = False
            elif event.type == QUIT:
                running = False
                