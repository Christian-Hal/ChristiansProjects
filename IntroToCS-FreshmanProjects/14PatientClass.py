#############################################################
#  Christian Hall
# date: 12/14/2022
# desc:
#############################################################

# The patient class has a name, age, and weight. Only the name and age
# are provided as arguments to the constructor. The weight is set to 150
# by default for all objects. A Patient also has an increaseAge function
# that increases the age by 1.
class Patient():
    def __init__(self, name, age, weight=150):
        self.name = name
        self.age = age
        self.weight = weight
        # this constructor takes in a name age and weight if no weight is put it will be set to 150

    @property
    def name(self):
        return self._name
    # name getter method

    @name.setter
    def name(self, newName):
        self._name = newName
    # name setter method

    @property
    def age(self):
        return self._age
    # age getter method

    @age.setter
    def age(self, newAge):
        if (newAge > 0):
            self._age = newAge
        else:
            self._age = 0
    # age setter method: it looks to see if the new age is negative if it is then it is set to 0

    @property
    def weight(self):
        return self._weight
    # weight getter method

    @weight.setter
    def weight(self, newWeight):
        if (0 <= newWeight <= 1400):
            self._weight = newWeight
        else:
            self._weight = self._weight
    # weight setter method... if the weight is outside the max and min it will not change otherwise it will set
    # newWeight to the current weight of that object

    def increaseAge(self):
        self.age += 1
    # this method increases the referenced patient object by 1


class In(Patient):
    def __init__(self, name, age, stay):
        super().__init__(name, age)
        self.stay = stay
    # Initialization function sends name and age to the super class then initializes stay as a variable of the In class

    @property
    def stay(self):
        return self._stay

    @stay.setter
    def stay(self, newStay):
        if(newStay > 0):
            self._stay = newStay
    # setters and getters for the stay class

    def __str__(self):
        return f"IN- \t{self.name} \t {str(self.age)}\t {str(self.weight)} \t {str(self.stay)}"
    # str magic function returns "IN-   My Name     26      150     5"


class Out(Patient):
    def __init__(self, name, age):
        super().__init__(name, age)
    # magic INIT function identifies object as Out and sends name and age to the patient class

    def __str__(self):
        return "OUT- \t" + self.name + "\t" + str(self.age) + "\t" + str(self.weight)
    # magic String function that allows you to print a patient of Out type


class ICU(In):
    def __init__(self, name, age, days=5):
        super().__init__(name, age, days)
        self.days = days
    # Init function gets needed info for ICU and Passes some of it to the in class


class CheckUp(Out):
    def __init__(self, name, age):
        super().__init__(name, age)
    # init function grabs needed info and passes it to superclass

################################################################
# ****    DO NOT MODIFY ANYTHING BELOW THIS POINT!    ****
# ################################ MAIN #########################


# Create three patient objects and print them out
p1 = Patient("Ben Dover", 22)
p2 = Patient("Helen Hywater", 16)
p3 = Patient("Amanda Lynn", 45)

print("\tName\t\tAge\tWeight")
print("-" * 40)
print("p1:\t{}\t{}\t{}".format(p1.name, p1.age, p1.weight))
print("p2:\t{}\t{}\t{}".format(p2.name, p2.age, p2.weight))
print("p3:\t{}\t{}\t{}".format(p3.name, p3.age, p3.weight))
print("-" * 40)

# Change their ages and print them out
p1.age = -5
p2.age = 100
p3.increaseAge()
p3.increaseAge()

print("p1:\t{}\t{}\t{}".format(p1.name, p1.age, p1.weight))
print("p2:\t{}\t{}\t{}".format(p2.name, p2.age, p2.weight))
print("p3:\t{}\t{}\t{}".format(p3.name, p3.age, p3.weight))
print("-" * 40)

# Change other instance variables and print them out
p1.weight = 2000
p2.name = "Justin Thyme"
p2.weight = 220
p3.weight = -50

print("p1:\t{}\t{}\t{}".format(p1.name, p1.age, p1.weight))
print("p2:\t{}\t{}\t{}".format(p2.name, p2.age, p2.weight))
print("p3:\t{}\t{}\t{}".format(p3.name, p3.age, p3.weight))
print("-" * 40)
