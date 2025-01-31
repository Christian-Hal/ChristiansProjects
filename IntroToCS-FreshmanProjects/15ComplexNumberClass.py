############################################################################
# name: Christian Hall
# date: 1/11/23
# description: Creates a complex number class which allows these "complex numbers" to be used in expressions outside
# the class
###########################################################################

# Don't forget to name this file Complex.py and place it in the same
# folder as the provided ComplexTest.py file so that they can
# automatically find and use each other.

class Complex:
    # A constructor that takes two values for the real and imaginary
    # portions respectively. Default values for both parameters are 0.
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

# ========= SETTERS / GETTERS ===========
    # Accessors and Mutators for the instance variables

    @property
    def real(self):
        return self._real
# get real number

    @real.setter
    def real(self, newReal):
        self._real = newReal
# set real number

    @property
    def imaginary(self):
        return self._imaginary
# get Complex imaginary number

    @imaginary.setter
    def imaginary(self, newImaginary):
        self._imaginary = newImaginary
# set Complex imaginary number

# ========== MAGIC FUNCTIONS ==========
    # Overloaded mathematical operators i.e. ==, +, -, *, /

    # adds 2 complex numbers together
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    # finds the difference between 2 complex numbers
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    # finds the product between 2 complex numbers
    # formula :::: a+bi * c+di = (ac - bd) + (ad + bc)i
    # there is a subtraction sign because the imaginary numbers are squared, so they will = -1
    def __mul__(self, other):
        tempReal = (self.real * other.real) - (self.imaginary * other.imaginary)
        tempImaginary = (self.real * other.imaginary) + (self.imaginary * other.real)
        return Complex(tempReal, tempImaginary)

    # divides two complex numbers together
    # I'm not gunna lie to you. I have no idea how to divide complex numbers.
    # I found line 48's formula on the internet, and I can not explain why it works
    #
    def __truediv__(self, other):
        return Complex(((self.real*other.real)+(self.imaginary*other.imaginary))/((other.real**2)+(other.imaginary**2)), ((self.imaginary*other.real)-(self.real*other.imaginary))/((other.real**2)+(other.imaginary**2)))

    # does complex number 1 equal complex number 2?
    def __eq__(self, other):
        if(self.real == other.real and self.imaginary == other.imaginary):
            return True
        return False

    # this will be called when you try to print a complex number
    def __str__(self):
        if(self.imaginary < 0):
            return str(self._real) + " - " + str(abs(self.imaginary)) + "i"
        else:
            return str(self._real) + " + " + str(abs(self.imaginary)) + "i"
# ====== USER DEFINED FUNCTIONS
    # Other functions e.g. reciprocal, conjugate, and __str__

    # returns a value with the imaginary value multiplied by -1 thus flipping the sign
    def conjugate(self):
        return Complex(self.real, -1 * self.imaginary)

    # to find the reciprocal you multiply 1/(a+bi) by the conjugate on top and bottom
    def reciprocal(self):
        return self.conjugate() / (self * self.conjugate())
