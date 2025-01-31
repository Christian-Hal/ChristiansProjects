# This function will be used to print out the correct
# conversion of units. It should take in two arguments
# based of those arguments, it should be able to convert into
# 4 different unit weights (including current unit).



# This fucntion should return 4 print statements with weight conversions.
def convertUnits(amount, unit):
    pound = ["pound", "pounds", "lb"]
    ounce = ["ounce", "ounces", "oz"]
    gram = ["gram", "grams", "g"]
    kilogram = ["kilogram", "kilograms", "kg"]

    if(unit in pound):
        amountPounds = amount
        amountOunce = amount * 16
        amountGram = amount * 453.59
        amountKilo = amount / 2.205

    elif(unit in ounce):
        amountPounds = amount / 16
        amountOunce = amount
        amountGram = amount * 28.34
        amountKilo = amount * 2834

    elif(unit in gram):
        amountPounds = amount * .00220462
        amountOunce = amount * 0.03527
        amountGram = amount
        amountKilo = amount / 1000
    elif(unit in kilogram):
        amountPounds = amount * 2.205
        amountOunce = amount * 35.274
        amountGram = amount * 1000
        amountKilo = amount
    else:
        print("this doesn't exist")
    try:
        print(amountKilo)
        print(amountGram)
        print(amountOunce)
        print(amountPounds)
    except:
        print("enter the right symbol")


########
# MAIN #
########

# DO NOT EDIT BELOW # 
weight = input("What would you like to convert? ")
amount, unit = weight.split(" ")
amount = int(amount)

convertUnits(amount, unit)
