##########################################################################
# author: Christian Hall
# date: 12/14/2022
# desc: gets a random list of a certain seed and then prints the first and last digit or the MSD and LSD
# then prints the results as listed in the rubric
#########################################################################
from random import randint, seed


SHOWLIST = False 	# a boolean to determine whether to show the list
MIN = 0			# the smallest random number that can be created.
MAX = 1000		# the largest random number that can be created.


# A function that prompts the user for two pieces of information i.e.
# the size of the list they want to create, and the seed that will be
# used for the list creation. It then returns both pieces of information to the
# calling statement.
def askForInfo():
    sizeAndSeed = [int(input("How big a list do you want to create? ")),
                   int(input("What seed should be used for its creation? "))]
    return sizeAndSeed


# A function that prints out a list. It receives two pieces of data. The
# first is a string representing the name of the list. The second is a
# list containing all the relevant data. It proceeds to print out the
# name, and then all the elements of the data separated using a tab
# space. Both the name and the entire list are printed on a single line.
def printList(listName, list):
    print(f"{listName}", end="\t")
    for value in list:
        print(value, end="\t")
    print()


# A function that creates the list of random numbers. It receives two
# arguments: one for the size of list to be created, and another for the
# seed that will be used to create the list. The function creates the
# list using the global variables MIN and MAX to form a bound for the
# kinds of numbers that are added to the list. The list is then returned
# to the calling statement.
def createList(size, runSeed):
    newList = []
    seed(runSeed)
    for i in range(size):
        newList.append(randint(MIN, MAX))
    return newList


# A function that receives a list of numbers and returns another list
# containing the frequency of the lists Most Significant Digits (MSD). The
# list created by the function has 10 elements with each value
# corresponding to a different possible MSD i.e. the value in index 0
# shows the number of values in the original number list that have 0 as
# their most significant digit; the value in index 1 shows the number of
# values with 1 as their MSD; and so on and so forth. This 10 element
# list is returned to the calling statement.
def findMSD(receivedList):
    MSDList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(receivedList)):
        MSDigit = str(receivedList[i])[0]
        MSDList[int(MSDigit)] += 1
    return MSDList


# Similar to the function above, a function that receives a list of
# numbers, and returns another list of 10 elements where each element
# represents the frequency of a specific Least Significant Digit in the
# original list.
def findLSD(receivedList):
    LSDList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(receivedList)):
        LSDigit = int(str(receivedList[i])[-1])
        LSDList[LSDigit] += 1
    return LSDList


# ##################################### MAIN ############################
# using the functions defined above:
#   prompt the user for the size of the list to be created as well as the seed.
lenAndSeed = askForInfo()

#   create the list of random numbers
randList = createList(lenAndSeed[0], lenAndSeed[1])

#   If SHOWLIST is selected, print out the list of numbers
if(SHOWLIST):
    print(f"Original List: \n{randList}")

#   print the head of the table which just shows the numbers 0-9
print("------------------------------------------------")
print("\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9")
print("------------------------------------------------")

#   Calculate the MSD and LSD, and print out their statistics.
MSDList = findMSD(randList)
LSDList = findLSD(randList)
printList("MSD", MSDList)
printList("LSD", LSDList)

#   Post code comment I really would comment my code, but you have legit explained everything that my code does already
#   there isn't anything else to explain
