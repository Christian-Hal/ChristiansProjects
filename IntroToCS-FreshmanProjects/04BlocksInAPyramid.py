#########################################################################
# name: Christian Hall
# date: 10/14/22
# description: Blocks In a Pyramid solution: this program has 3 functions that all serve to help calculate
# the amount of 1x1 blocks in a pyramid of x height assuming that the amount of blocks on 1 layer
# is equal to the layer squared
#########################################################################

# A function to prompt the user for the number of levels that their
# pyramid will have and return it to the calling statement.
def totalLevels():
    layers = int(input("How many levels will your pyramid have? "))
    return layers


# A function that receives the number of pyramid levels and the number
# of blocks as arguments, and prints the appropriate results to the
# screen.
def printTotal(layers, blocks):
    print(f"For {layers} levels, you will need {blocks} blocks")


# A recursive function that receives the number of the level, calculates
# the number of blocks required, and returns the result to the calling
# statement.

def totalBlocks(layers, blocks):
    if layers <= -1:
        return 0

    if layers == 0:
        return blocks - 1
    blocks += layers * layers
    return totalBlocks((layers - 1), blocks)


################################ MAIN ################################
# using the function(s) defined above, ask the user for the number of
# pyramid levels
levels = totalLevels()
blocks = totalBlocks(levels, 1)
# using the function(s) defined above, calculate and display the final results
printTotal(levels, blocks)
