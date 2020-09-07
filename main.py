#!/usr/bin/python3

from polynomial import Polynomial
from integration import RectIntegration, TrapIntegration, ExactIntegration

print("Welcome to the integration calculator ")
exit = False

while not exit:
    degree = int(input("Please enter the degree of the polynomial: "))
    polynomial = Polynomial(degree)
    raw_coef = []
    while not len(raw_coef) == degree + 1:
      raw_coef = input("Please enter the coeficiants seperated by spaces: ")
      raw_coef = raw_coef.split(" ")

      coef = [float(x) for x in raw_coef]
    polynomial.setCoef(coef)
    raw_lower = input("What is the lower bound: ")
    raw_upper = input("What is the upper bound: ")
    lower = int(raw_lower)
    upper = int(raw_upper)
    method = 0
    while not method or method > 3 or method < 0:
        raw_method = input(
            "Please choose 1. Rectangular, 2. Trapezoid, 3. Exact: ")
        method = int(raw_method)
    if method != 3:
        raw_n = input("Please choose n: ")
        n = int(raw_n)
    if method == 1:
        results = RectIntegration.evalLeft(lower, upper, n, polynomial)
    elif method == 2:
        results = TrapIntegration.evaluate(lower, upper, n, polynomial)
    elif method == 3:
        results = ExactIntegration.evaluate(lower, upper, polynomial)
    print(results)
    raw_exit = input("Would you like to do another calculation? y or n?: ")
    if raw_exit[0] == 'n' or raw_exit[0] == 'N':
        exit = True