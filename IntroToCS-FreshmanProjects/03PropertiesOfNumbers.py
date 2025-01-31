#################################################################################
# name: Christian Hall
# date: 10/10/2022
# description: Number properties assignment
#################################################################################

# A function that prompts the user for a number and returns it.
def getNum():
    num1 = int(input("Enter a number: \t"))     # super simple! just use input to create an int variable and return that
    return num1                                 # variable


# A function that receives two numbers as arguments, and returns the
# larger of the two numbers.
def maxOf2(num1, num2):     # this user defined function runs slower than the regular max() command, but it seems
    if num1 >= num2:        # intuitive enough to me! 1 if statement with 2 possible return values
        return num1
    else:
        return num2


# A function that receives three numbers as arguments, and returns the
# largest of the three numbers.
def maxOf3(num1, num2, num3):           # this effectively does the same thing that my maxOf2() function does by taking
    relativeMax = maxOf2(num1, num2)    # 2 variables and then finding the larger. The only change is that I have a
    if relativeMax >= num3:             # third variable that
        return relativeMax
    else:
        return num3


# A function that receives three numbers as arguments, and returns the
# product of the two largest arguments.
def largestProduct(num1, num2, num3):
    largestNum = maxOf3(num1, num2, num3)   # I really dislike this code. It seems more intuitive to use a list but
    if num1 == largestNum:                  # alas I must obey the overlords known as the grading rubric. If you are
        return maxOf2(num2, num3) * num1    # wanting a better solution to this problem then you can check out the
    elif num2 == largestNum:                # section underneath this function... Anyway I find the largest number
        return maxOf2(num1, num3) * num2    # then compare it to each of the numbers since I don't know which variable
    else:                                   # is the largest. When I find the largest variable I then multiply it by
        return maxOf2(num1, num2) * num3    # the largest value of the other two variables


'''
numList = [num1, num2, num3]
numList.sort()
return numList[1] * numList[2]
'''

# A function that receives an argument and returns a string representing
# whether that argument is even or odd.
def evenOrOdd(num1):
    if num1 % 2 == 0:   # first you test to see if the number is divisible by two
        return "Even"   # if it is return even if not return odd
    else:
        return "Odd"


# A function that receives an argument and determines whether that
# argument is a prime number.
def isPrime(num1):
    primeTest = num1 - 1                # I think this code is rather pretty first I test to see if the number is
    if primeTest >= 0:                  # positive or negative. negative numbers are always Not prime (unless you
        while primeTest > 1:            # change the rules for them) so I set the value as false for all numbers less
            if num1 % primeTest == 0:   # then 0 after which it divides all numbers
                return False            # the problem is that this code is terribly slow and there are ways to
            primeTest -= 1              # speed it up at the expense of more lines of code input 39916801
    primeTest = num1 + 1                # just to see how slow it is
    if primeTest < 0:                   # this is because I divide the number by itself - 1 as many times as it takes to
        return False                    # get to 0
    return True



# Functions that were defined above should be executed below in an order
# that satisfies the original problem statement. Additional statements
# can be included if needed.
##########################################################################

# Prompt for three different numbers and store them appropriately.
firstInput = getNum()   # pretty standard... starting code by defining variables
secondInput = getNum()
thirdInput = getNum()

# Print out the table header information.

if len(str(firstInput)) >= 8 or len(str(secondInput)) >= 8 or len(str(thirdInput)) >= 8: # all if statements are for format
    print('''---------------------
NUM\t\t\tEVEN\tPRIME
---------------------''')

elif len(str(firstInput)) >= 4 or len(str(secondInput)) >= 4 or len(str(thirdInput)) >= 4:
    print('''---------------------
NUM\t\tEVEN\tPRIME
---------------------''')

else:
    print('''---------------------
NUM\tEVEN\tPRIME
---------------------''')

# Print out the table contents for each of the three numbers.
print(str(firstInput) + "\t" + evenOrOdd(firstInput) + " \t" + str(isPrime(firstInput)))  # this prints all number properties
print(str(secondInput) + "\t" + evenOrOdd(secondInput) + " \t" + str(isPrime(secondInput))) # the rubric asks me to print
print(str(thirdInput) + "\t" + evenOrOdd(thirdInput) + " \t" + str(isPrime(thirdInput)))

# Print out the identity of the largest number and the largest product
# from the given numbers.
print("---------------------")
print("The largest number is " + str(maxOf3(firstInput, secondInput, thirdInput)))                      # keep it simple
print("The largest possible product is " + str(largestProduct(firstInput, secondInput, thirdInput)))

# I use user defined functions along with prints to show the largest number of the three and the largest product of the
# three numbers
