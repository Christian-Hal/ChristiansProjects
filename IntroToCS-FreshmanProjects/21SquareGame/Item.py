#####################################################################
# author: Christian Hall
# date: 3/10/2023
# description: Creates a person class and places them on a grid. Functions in this class can move the objects around
# the grid
#####################################################################

# global Constants to restrict the maximum x and y values that a person object
# can have.
MAX_X = 800
MAX_Y = 600

# A class representing a person. A person can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left, 
# go right, go up and go down. A person also has a string function 
# that prints out their name location, and size. A person also has a 
# function that calculates the euclidean distance from another person 
# object.
class Item:
    def __init__(self, name="player 1", xCoord=0, yCoord=0, size=1.0):
        self.name = name
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.size = size

# setters and getters...
    # for name
    @property
    def name(self):
        return self._name

    # name setter defaults to player 1 if the length of input string is less than 2 characters
    @name.setter
    def name(self, value):
        if (len(value) >= 2):
            self._name = value
        else:
            self._name = "player 1"

    # for xCoord
    @property
    def xCoord(self):
        return self._xCoord

    # xCoord setter will only set to given value if it is greater than 0 and less than the max value of x
    # else it will set it to 0 or the max value of x respectively
    @xCoord.setter
    def xCoord(self, value):
        if(0 < value <= MAX_X):
            self._xCoord = value
        elif(value > MAX_X):
            self._xCoord = MAX_X
        else:
            self._xCoord = 0

    # for yCoord
    @property
    def yCoord(self):
        return self._yCoord

    # see xCoord setter for description
    @yCoord.setter
    def yCoord(self, value):
        if(0 < value <= MAX_Y):
            self._yCoord = value
        elif (value > MAX_Y):
            self._yCoord = MAX_Y
        else:
            self._yCoord = 0

    # for size
    @property
    def size(self):
        return self._size

    # the rubric wanted size as a double it also cannot be negative else it defaults to 1
    @size.setter
    def size(self, value):
        if(value > 0):
            self._size = value
        else:
            self._size = 1

# User defined functions
    # if this is a grid when this function is called a person object gets moved to the left on the grid (or in
    # negative direction)
    def goLeft(self, distance=1):
        self.xCoord -= distance

    # if grid then called function moves person object to right on grid (or in a negative direction)
    def goRight(self, distance=1):
        self.xCoord += distance

    # moves person object up (or in positive direction)
    def goUp(self, distance=1):
        self.yCoord -= distance

    # moves person object down (or in negative direction)
    def goDown(self, distance=1):
        self.yCoord += distance

    # takes a person object and then finds the distance from another person
    def getDistance(self, person):
        return ((self.xCoord - person.xCoord) ** 2 + (self.yCoord - person.yCoord) ** 2) ** .5

    # function gets called when you attempt to print an object it prints in the format...
    # "Person(player 1): size = 1,  x = 1   y = 1"
    def __str__(self):
        return f"Person({self.name}):\tsize = {self.size},\tx = {self.xCoord}\ty = {self.yCoord}"
