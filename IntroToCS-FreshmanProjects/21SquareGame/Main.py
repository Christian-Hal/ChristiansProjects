#####################################################################
# author: Christian Hall
# date: 3/27/2023
# description: This creates a pygame window and then draws a rectangle which can be moved around
# said rectangle also can change color and size when the space key is pressed.
#####################################################################
from pygame import *
from random import randint, choice
from Item import *
from Constants import *

# Class person which is a subclass for the superclasses Item and Sprite
class Person(pygame.sprite.Sprite, Item):
    # The Init function calls the two superclasses it also will call some other functions to
    # force the square to be drawn at a random position
    def __init__(self, color=RED):
        Item.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.setRandomPosition()
        self.setSize()
        self.color = color
        self.surf.fill(color)

    # Calls the constants file and sets one of the colors in the list to the color and
    # fills the rectangle with said color
    def setColor(self):
        self.color = choice(COLORS)
        self.surf.fill(self.color)

    # takes a random size from 1 to 10 and then resizes the rectangle to the rectangles size
    def setSize(self):
        self.size = randint(10, 100)
        self.surf = pygame.Surface((self.size, self.size))

    # calls different functions when a specific key is pressed
    def update(self, pressed_keys):
        # when the Up key is pressed go up
        if pressed_keys[K_UP]:
            self.goUp()
        # when down is pressed... ect
        if pressed_keys[K_DOWN]:
            self.goDown()
        if pressed_keys[K_LEFT]:
            self.goLeft()
        if pressed_keys[K_RIGHT]:
            self.goRight()
        # when Space is pressed change the color and set the size to a random size from 10,100
        if pressed_keys[K_SPACE]:
            self.setSize()
            self.setColor()
        pass

    # sets the xCoord and yCoord to a random position
    def setRandomPosition(self):
        self.xCoord = randint(0, MAX_X)
        self.yCoord = randint(0, MAX_Y)

    # used to set the x and y coord to the correct position
    def getPosition(self):
        return [self.xCoord, self.yCoord]

    # whenever the space key is pressed the toString gets called which will bring the location name and color of the
    # person object that is being called
    def __str__(self):
        return f"Person({self.name}):\tsize = {self.size},\tx = {self.xCoord}\ty = {self.yCoord}" + f"\tcolor: {str(self.color)}"


# ########################## main game ################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#####################################################################


# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a person object
p = Person()
RUNNING = True
# A variable to determine whether to get out of the
# infinite game loop

while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            print(p)

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()

    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    p.update(pressedKeys)

    # fill the screen with a color
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()
