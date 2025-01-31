################################################################################
# Name:   Christian Hall
# Date: 9/30/22
# Description:
################################################################################

# A function that prompts the user for a name and returns it to the
# calling statement.

def getName():                                  # asks user for string input
    name = input("Please enter your name: ")    # saves it as string
    return name                                 # returns name as string

# A function that prompts the user for a score and returns it to the
# calling statement.

def getScore():                             # asks user for numerical input
    num = int(input("Enter your score: "))  # changes string to int then
    return num                              # returns num as an int


# A function that receives two numbers and returns the average of those
# two values to the calling statement.

def getAverage(var1, var2):         # function calculates the average
    average = (var1 + var2) / 2     # by taking 2 variables and adding them together
    return average                  # then dividing by two then returning the value

# A function that receives a string and a number (the name and the
# average score) and prints it out on the screen in the appropriate format.
def printOutput(givenName, averageScore):
    print(f"Hi, {givenName}. Your average score was {averageScore}")

#############################################################################
#       MAIN PART OF PROGRAM
# Functions that were defined above should be executed below in an order
# that satisfies the problem statement. Additional statements can be
# included below as well if needed.
#############################################################################

# prompt for name
name = getName()

# prompt for two scores
score1 = getScore()
score2 = getScore()

# calculate the average
average = getAverage(score1, score2)
# display the final output
printOutput(name, average)

