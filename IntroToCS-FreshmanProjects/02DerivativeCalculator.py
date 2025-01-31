# derivative calculator
H = 0.0000000001


def f(x):
    return 2 * (x ** 2) + (7 * x) + 9
# put function here


def derivative():
    x = float(input("What is value X: "))
    return (f(x + H) - f(x))/H


'''
lim h->0 f(x + h) + f(x)/h
'''

print(derivative())