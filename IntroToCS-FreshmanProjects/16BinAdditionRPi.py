#################################################################
# Name: Christian Hall
# Date: 1/27/2023
# Description: Takes 2 random binary integers and adds them together
#################################################################
import RPi.GPIO as GPIO # bring in GPIO functionality
from random import randint # to generate random integers

def setGPIO():
    # define the pins (change these if they are different)
    gpio = [19, 20, 21, 22, 23, 24, 25, 26, 27]
    # set them up as output pins   
    GPIO.setup(gpio, GPIO.OUT)
    return gpio

def setNum():
    # create an empty list to represent the bits
    num = []
    # generate eight random bits
    for i in range(0, 8):
        # append a random bit (0 or 1) to the end of the list
        num.append(randint(0, 1))
    return num

def display():
    for i in range(len(sum)):
        # if the i-th bit is 1, then turn the i-th LED on
        if (sum[i] == 1):
            GPIO.output(gpio[i], GPIO.HIGH)
    # otherwise, turn it off
        else:
            GPIO.output(gpio[i], GPIO.LOW)

def fullAdder(Cin, A, B):
    S1 = A ^ B # xor gate calculates the sum
    C1 = A & B # and gate calcultes the carry
    # ^ this is the first half adder

    S = Cin ^ S1
    C2 = Cin & S1
    # ^ this is the second half adder
    Cout = C1 | C2
    # ^ ensures the carry is correct at the very end
    
    return S, Cout

def calculate(num1, num2):
    Cout = 0 # the initial Cout is 0
    sum = [] # initialize the sum
    n = len(num1) - 1 # position of the right-most bit of num1
    # step through each bit, from right-to-left
    while (n >= 0):
        # isolate A and B (the current bits of num1 and num2)
        A = num1[n]
        B = num2[n]
        # set the Cin (as the previous half adder's Cout)
        Cin = Cout
        # call the fullAdder function that takes Cin, A, and...
        # ...B, and returns S and Cout
        S, Cout = fullAdder(Cin, A, B)
        # insert sum bit, S, at the beginning (index 0) of sum
        sum.insert(0, S)
        # go to the next bit position (to the left)
        n -= 1

    # insert the final carry out at the beginning of the sum
    sum.insert(0, Cout)

    return sum

GPIO.setmode(GPIO.BCM)
# setup the GPIO pins
gpio = setGPIO()
# get a random num1 and display it to the console
num1 = setNum()
print("     ", num1)
# get a random num2 and display it to the console
num2 = setNum()
print("+    ", num2)
# calculate the sum of num1 + num2 and display it to the console
sum = calculate(num1, num2)
print("= ", sum)
# turn on the appropriate LEDs to "display" the sum
display()
# wait for user input before cleaning up and resetting GPIO pins
input("Press ENTER to terminate")
GPIO.cleanup()