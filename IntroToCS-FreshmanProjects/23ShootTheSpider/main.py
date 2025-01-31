# #########################################################################
# Name: Christian Hall
# Date: 4/15/2023
# Description: Creates a gui with 3 sprites. A wizard, a spider and a bullet... you shoot the spider with the bullet
# if it hits it increases your score by one and resets the positon of the spider. otherwise if the spider gets to the
# right side of the screen it decreases you lives by one... if lives get to 0 you lose and the game crashes
# #########################################################################
# NOTE: I AM NOT USING THE MOVING SQUARE TEMPLATE FOR THIS ASSIGNMENT i want to complete this
# assignment in a fashion i enjoy
# the rubric will be followed but the assigned guide will only be occasionally refrenced

import pygame
from pygame.locals import *
from random import randint

LENGTH = 600
WIDTH = 400
SCORE = 0
LIVES = 3


class Sprite(pygame.sprite.Sprite):
    def __init__(self, xCoord, yCoord, imageName):
        super(Sprite, self).__init__()
        self.surf = pygame.image.load(imageName).convert()
        self.rect = self.surf.get_rect()
        self.xCoord = xCoord
        self.yCoord = yCoord

    @property
    def xCoord(self):
        return self._xCoord

    @xCoord.setter
    def xCoord(self, value):
        if (-70 < value < WIDTH+120):
            self._xCoord = value

    @property
    def yCoord(self):
        return self._yCoord

    @yCoord.setter
    def yCoord(self, value):
        if(0 < value < LENGTH):
            self._yCoord = value

    # USER DEFINED FUNCTIONS
    # causes the wizard and bullet to move when A and D are pressed
    def move(self, keys):
        if keys[K_a]:
            self.xCoord -= .1
        if keys[K_d]:
            self.xCoord += .1

    # ONLY FOR THE BULLET SPRITE
    # IF THE BULLET IS NOT BEING FIRED ALREADY set boolean value that causes the bullet to start moving up to true
    def fire(self):
        if(self.yCoord <= 1):
            self.yCoord = wizard.yCoord
            self.xCoord = wizard.xCoord
            return False
        else:
            return True

    # ONLY FOR THE SPIDER SPRITE
    # imagine a 40 unit box around the spider... if the other sprite in collision is within that 40 block radii then
    # move the spider back to the start... if the spider is hit... increase the score
    def detectCol(self, other, score):
        if(other.yCoord - self.yCoord <= 40 and self.yCoord - other.yCoord <= 40
                and other.xCoord - self.xCoord <= 40 and self.xCoord - other.xCoord <= 40):
            self.backToStart()
            print(f"Total Score {score + 1}")
            return score + 1
        return score

    # moves the spider back to the start
    def backToStart(self):
        self.xCoord = -69
        self.yCoord = randint(0, LENGTH-150)

    # causes constant movement of the spider
    def moveSpider(self, score):
        self.xCoord += .02 + (score / 500)

# initialize pygame and set up all the sprites
pygame.init()

screen = pygame.display.set_mode([WIDTH, LENGTH])

wizard = Sprite(WIDTH/2, LENGTH-80, "wizard.png")
spider = Sprite(-69, randint(0, LENGTH-150), "spider.png")
bullet = Sprite(wizard.xCoord, wizard.yCoord, "bullet.png")
isFire = False

running = True
while(running):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

        if (event.type == KEYDOWN):
            if (event.key == K_SPACE):
                isFire = bullet.fire()

    pressedKeys = pygame.key.get_pressed()
    wizard.move(pressedKeys)

    # All bullet logic...
    # What needs to happen is when isFire = false it follows the wizard otherwise move the bullet up a bit
    if(isFire == False):
        bullet.move(pressedKeys)
    elif(isFire == True):
        bullet.yCoord -= 1
    if(isFire == True and bullet.yCoord <= 1):
        isFire = False
        bullet.yCoord = wizard.yCoord
        bullet.xCoord = wizard.xCoord

    # All spider logic...
    # move the spider constantly over a small amount and make it get faster as the score increases
    # if you fail to hit the spider the score does not increase and you take a decrease to your lives
    spider.moveSpider(SCORE)
    if (spider.xCoord >= WIDTH + 119):
        spider.backToStart()
        LIVES -= 1
        print(f"Lives left: {LIVES}")
    SCORE = spider.detectCol(bullet, SCORE)

    # Quit when the spider makes it to the right side of the screen for the 3rd time and lives == 0
    if LIVES == 0:
        running = False

    screen.fill((255, 255, 255))

    # show the sprites
    screen.blit(bullet.surf, (bullet.xCoord, bullet.yCoord))
    screen.blit(spider.surf, (spider.xCoord, spider.yCoord))
    screen.blit(wizard.surf, (wizard.xCoord, wizard.yCoord))

    pygame.display.flip()
