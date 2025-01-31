from enchant import *
from tkinter import *


# This function returns all the info that is required for the assignment for both string and int
def enchantStuff(numOrString):
    word = Dict("En_US")
    SuggestArray = []

    # if the code cannot change numOrString into an int type number than it must be a string
    try:
        numOrString = float(numOrString)
    except:
        pass

    # If it is still a string type and not an actual english word then create an array for possible words you could
    # have wanted to use instead
    if (type(numOrString) == str and not word.check(numOrString)):
        SuggestArray = word.suggest(numOrString)

    # if the number is a float type, then (if it's able) convert it to a string (if it's not) read it as a decimal
    # number. then, run some tests to see if its prime and odd or not and return that information
    if (type(numOrString) == float):
        if(numOrString % 1 == 0):
            return f"NUMBER\nInteger.\n{isOdd(numOrString)}\n{isPrime(numOrString)}"
        else:
            return "NUMBER\nDecimal."

    # the only thing remaining is string values now you format the strings as wanted in the rubric
    elif(word.check(numOrString)):
        return f"STRING\n{len(numOrString)} characters\nValid English word"
    else:
        return f"STRING\n{len(numOrString)} characters\nClose English words include\n{SuggestArray}"

# prime tester
def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

# even or odd tester
def isOdd(n):
    if(n % 2 == 0):
        return "Even"
    return "Odd"


window = Tk()

# My birthday present from zak! I love you so much.
def frameOne(f2:Frame):
    if f2:
        f2.destroy()
    f1 = Frame(window)

    e1 = Entry(f1)
    e1.grid(row=0, column=0, sticky=N + E)

    b1 = Button(f1, text="Analyze", command=lambda: frameTwo(f1, e1.get()))
    b1.grid(row=0, column=1)
    f1.pack()

def frameTwo(f1:Frame, info):
    f1.destroy()
    f2 = Frame(window)

    l1 = Label(f2, text=enchantStuff(info), wraplength=200, justify=LEFT)
    l1.grid(row=0, column=0)

    b1 = Button(f2, text="Another One", command=lambda: frameOne(f2))
    b1.grid(row=0, column=1)
    f2.pack()


frameOne(None)
window.geometry("400x200")
window.mainloop()
