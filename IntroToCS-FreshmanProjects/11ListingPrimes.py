#######################################################################
# author: Christian Hall
# date: 12/2/2022
# desc: takes any integer input and returns all prime numbers from 0 to that input
########################################################################


# A function to prompt the user for a number and return that value to
# the calling statement.
def getInput():
    return int(input("What limit are you interested in? "))


# A function that receives a number and tests that number to see whether
# it is prime or not. It returns the boolean response to the calling
# statement.
def isPrime(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:    # this sees if the number is divisible by any other number than 1
            return False
    return True
# ################# MAIN ######################################
# Using the functions declared above, ask the user for a number, then
# create a list of all the prime numbers less than that number. Proceed
# to print out the relevant information related to that list.


allPrimes = []
upperBound = getInput()
count = 0   # initializing variables

for i in range(2, upperBound):  # for all numbers from 2 to upper bound...
    if isPrime(i):  # how many are prime?
        allPrimes.append(i)
        count += 1  # add 1 number to the primes list and add 1 to count
print(f"There are {count} prime numbers less than {upperBound}")    # finally print both the prime list and how many...
print(allPrimes)    # primes are between 0 and upperBound
