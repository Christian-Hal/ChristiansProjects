######################################################################
# author: Christian Hall
# date: 2/1/2023
# desc: Creates a "Game" that
#####################################################################
from random import randint, seed


def refreshArray(arr, length):
    arr.clear()
    for i in range(length):
        arr.append(i+1)
    return arr


DEBUG = False  # Activate intermediate output


# Initializing variables that I will need later in the program
correct = 0
correctArray = []
simScore = []
passedTests = 0

# Most of the setup for the rest of the program happens here
print("Simulation Set Up:\n"
      "=================================================================")

# Initialize the bank and creates an array of the users choice
bankSize = int(input("What is the size of the question bank? "))
bankArray = []
refreshArray(bankArray, bankSize)

# Asks how many questions the user studied and initializes an array for later use
studySize = int(input("How many of those questions have you studied? "))
studyArray = []

# Asks how many questions will be on the test an initializes an array for later use
testSize = int(input("How many questions does the test have? "))
testArray = []

# gets an int the int is then checked to see if it is larger than the simulations score if it isn't the sim passes
neededRight = int(input("How many questions must you answer correctly to pass the test? "))

print("=================================================================")
totalSims = int(input("How many simulations do you want to run? "))
print("=================================================================")

# master for loop that runs all the simulations
for i in range(totalSims):
    # for each test question pull a certain number of questions from the bank
    for j in range(testSize):
        randomNum = randint(0, len(bankArray) - 1)
        testArray.append(bankArray[randomNum])
        bankArray.pop(randomNum)
    # if debug is true print some extra stuff
    if DEBUG:
        print("Simulation No. " + str(i + 1))
        print(f"Questions you were asked: {testArray}")

    # reset the bank array
    refreshArray(bankArray, bankSize)
    # pull a certain number of questions from the bank into a study list

    for j in range(studySize):
        randomNum = randint(0, len(bankArray) - 1)
        studyArray.append(bankArray[randomNum])
        bankArray.pop(randomNum)

    # if the number at index j is in the study array... that counts as a correct question
    for j in range(len(testArray)):
        if (testArray[j] in studyArray):
            correct += 1
            correctArray.append(testArray[j])

    # if debug print
    if DEBUG:
        print(f"Questions you Studied: {studyArray}")
        print(f"Questions you passed: {correctArray}")
        print(f"Which means you scored {correct}/{testSize}")
        print("-----------------------------------------------------------------")

    # refresh everything for the next sim and save whether this sim was a success or failure
    simScore.append(correct)
    refreshArray(bankArray, bankSize)
    testArray.clear()
    studyArray.clear()
    correctArray.clear()
    correct = 0

# more if debug print
if DEBUG:
    print("Simulation scores were:")
    print(simScore)
    print("=================================================================")

# counts the total number of passed sims
for sims in simScore:
    if(neededRight <= sims):
        passedTests += 1

# states the % of passed to taken
print(f"You passed the test {(passedTests/totalSims)*100}% of the time")
