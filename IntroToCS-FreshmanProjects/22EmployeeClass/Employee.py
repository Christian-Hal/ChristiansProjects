#####################################################################
# author: Christian Hall
# date: 4/6/2023
# description: Create a class titled Employee that has the functions specified in the
# rubric... Running the file "03 test_Employee.py" will call all the functions
# from this class and test them. Any failed tests will show up in the terminal
#####################################################################

# import the abc library to make abstract classes
from abc import ABC, abstractmethod

######################################################################
# An employee class. Its constructor takes the first name, last name and
# pay. It also has email and position as instance variables. It contains
# a single abstract method i.e. applyRaise, and a createEmail function
# that creates an appropriate email address from the employee's first
# and last names.
######################################################################
class Employee(ABC):
    # Abstract class Employee that will be used as a superclass for 2 other subclasses
    def __init__(self, fName, lName, pay):
        self.firstname = fName
        self.lastname = lName
        self.pay = pay
        self.email = self.createEmail()
        self.position = None

    # past this line lies the setters and getters each with their own subprocesses and requirements
    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        self._firstname = value.title()
        self._firstname = self._firstname.replace(" ", "")

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        self._lastname = value.title()
        self._lastname = self._lastname.replace(" ", "")

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def pay(self):
        return self._pay

    @pay.setter
    def pay(self, value):
        if(value < 20000):
            self._pay = 20000
        else:
            self._pay = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if("@latech.edu" in value):
          self._email = value
        else:
            self._email = f"{self.firstname.lower()}.{self.lastname.lower()}@latech.edu"

    # USER DEFINED FUNCTIONS
    def createEmail(self):
        return f"{self.firstname.lower()}.{self.lastname.lower()}@latech.edu"

    @abstractmethod
    def applyRaise(self, value):
        raise NotImplementedError

    # toString function. When an employee or staff is attempted to be cast to a string
    # it will return as "lastname, firstname (email)"
    def __str__(self):
        return f"{self.lastname}, {self.firstname} ({self.email})"

######################################################################
# A faculty class is a subclass of the Employee class above. Its
# constructor receives both names as well as the position. The Faculty
# class also overrides the applyRaise function by multiplying the pay by
# the rate provided as an argument. It also slightly tweaks the __str__
# function in the super class.
######################################################################
class Faculty(Employee):
    def __init__(self, fName, lName, position):
        super().__init__(fName, lName, 50000)
        self.position = position

    def applyRaise(self, value):
        if(value >= 0):
            self.pay *= value

    def __str__(self):
        return f"{self.lastname}, {self.firstname} ({self.email}) -- {self.position}"


######################################################################
# A Staff class is a subclass of the Employee class above. Its
# constructor only receives both names. It also overrides the applyraise
# function but adding the increase (provided as the argument) to the
# pay. It doesn't change anything else from the Employee class.
######################################################################
class Staff(Employee):
    def __init__(self, fName, lName):
        super().__init__(fName, lName, 40000)

    def applyRaise(self, value):
        if(value >= 0):
            self.pay += value
