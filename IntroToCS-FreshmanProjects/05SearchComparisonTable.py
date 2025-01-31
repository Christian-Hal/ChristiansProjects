##########################################################################################
# Name: Christian Hall
# Date: 10/27/2022
# Description: if I were to print a list of numbers on average how many iterations it takes for that list to be searched
# sequentially and then binary-ly then divide the answers by themselves
##########################################################################################
import math     # what is this doing here??? Who are you? What are you doing? I don't need you!


# a function that displays the table
def displayTable(x, y, z):
    print(f"{'n' : <8}{'seq' : <8}{'bin' : <8}{'Perf'}")    # formats the program to always have the same spacing
    print("----------------------------")                   # then uses a for loop to print all the correct averages
    for i in range(x, y + 1, z):
        performance = 0
        if i != 0:
            performance = int(sequentialAverage(i)/binaryAverage(i))
        print(f"{i : <8}{sequentialAverage(i) : <8}{binaryAverage(i) : <8}" + str(performance))


'''you must display the whole table using the displayTable() function'''    # which I did


# a function that calculates the average number of comparisons of a sequential search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def sequentialAverage(n):   # int truncates the number so by adding .5 to the total im effectively saying round up!
    return int(n/2 + .5)    # which gives me the desired answer to sequential's average


# a function that calculates the maximum number of comparisons of a binary search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def binaryAverage(n):
    if n == 0:
        return 0
    return int(math.log(n, 2) + 1)  # wait what's that thing??? log? huh? what is log?
# yeah, I used the math function cuz I didn't want to do something like 1/(2**n) or whatever the equal expression would
# have been I knew that the average was log_2(n) so that's what I put


###############################################
# MAIN PART OF THE PROGRAM
###############################################
# get user input for the minimum (make sure that it is >= 0)
while True:
    minVal = int(input("Minimum number of list items (>=0)? "))  # ask the user for an input
    if minVal < 0:
        print(" *ERROR: Minimum must be >= 0!")  # and as long as that input is greater than 0
    else:
        break   # you will break from the while True


# get user input for the maximum (make sure that is is >= minimum)
while True:
    maxVal = int(input("Maximum number of list items (>= min (100))? "))    # ask the user for an input
    if maxVal < minVal:
        print(" *ERROR: Maximum must be >= minimum (100)!")  # and as long as the input is greater than the minimum
    else:
        break   # you break from the while True

# get user input for the interval (make sure that it is >= 1)
while True:
    increase = int(input("The interval between each row of the table (>= 1)? ")) # ask the user for an input
    if increase < 1:
        print(" *ERROR: Interval must be >= 1!") # and as long as the input is greater than 1
    else:
        break # you break from the code


# generate the table
displayTable(minVal, maxVal, increase)  # calls the displayTable() function
