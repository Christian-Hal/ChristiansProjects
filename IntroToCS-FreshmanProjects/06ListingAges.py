##############################################################################
# author: Christian Hall
# date:  11/1/2020
# description: This program gets a total number of people then asks for their name and age
# after which it will look through created lists of ages and names and find the average age along with the max age
# and minimum age with the persons name to accompany their age
#############################################################################

# A function that prompts the user for the number of people this program
# will be comparing.
def getTotalPeople():
    return int(input("How many people are you comparing? "))    # returns number of items in nameList and ageList


# A function that receives the size of a list, and repeatedly prompts the user
# for that number of names. It then returns the complete list of names.
def createNameList(listSize):
    nameList = []
    for i in range(listSize):                                           # creates a list called nameList and adds a new
        newName = input(f"What is the name of person number {i + 1}:")  # name which is given by the user for however
        nameList.append(newName)                                        # many indexes are supposed to be in this list
    return nameList                                                     # then returns the list "nameList"


# A function that receives the size of a list, and repeatedly prompts
# the user for that number of ages. It then returns the complete list of
# ages.
def createAgeList(listSize):
    ageList = []
    for i in range(listSize):                                               # does the same thing as nameList however
        newAge = int(input(f"What is the age of person number {i + 1}: "))  # this list only will accept integers but
        ageList.append(newAge)                                              # will add however many ints to the list
    return ageList                                                          # as requested. then returns the list.


# ------------------------------ MAIN ----------------------------------
# Ask for the number of people using one of the functions defined above.
while True:
    numPeople = getTotalPeople()                            # uses getTotalPeople function to get the list size for all
    if numPeople >= 1:                                      # future functions. however this value must be greater than
        break                                               # 0 or else the code breaks, so lines 38 40 and 41 help fix
    print("Please choose a number that is greater than 0")  # that problem
print("----------------------------------------")

# Ask for the names of the people using one of the functions defined
# above.
nameList = createNameList(numPeople)                        # creates a list using the name list function referenced
print("----------------------------------------")           # in line 19

# Ask for the ages of the people using one of the functions defined
# above.
ageList = createAgeList(numPeople)                          # creates a list using the age list function referenced
print("----------------------------------------")           # on line 30

# Identify the names of the youngest and oldest people in the list.
youngest = ageList.index(min(ageList))
oldest = ageList.index(max(ageList))

# Display information about the lists.
print(f"{nameList[youngest]} is the youngest at {ageList[youngest]} years old") # these lines find the minimum and max
                                                                                # values of ageList and then print the
                                                                                # age and name of the person who that
print(f"{nameList[oldest]} is the oldest at {ageList[oldest]} years old")       # value belongs to. Then it finds the
                                                                                # average of all the ages and prints
print(f"The average age is {sum(ageList)/len(ageList)}")                        # that value.
