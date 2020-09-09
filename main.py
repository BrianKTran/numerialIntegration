#!/usr/bin/python3

from polynomial import Polynomial
from integration import RectIntegration, TrapIntegration, ExactIntegration

print("Welcome to the Numerical Integration Computer! \nGiven the degree, coeffecients, lower bound, upper bound and number of subdivisions of any polynomial, \nthis program will compute the Rectangular, Trapezoidal and Exact Integrals of any polynomial! \nEnjoy! \nHappy Calc-ing! ")
exit = False

# Continuous While Loop for prompts the user for inputs 
while not exit:
    # Prompts user for object degree of a polynomial
    degree = int(input("Please enter the degree of the polynomial: "))
    # variable for new polynimial function with given degree passed in
    polynomial = Polynomial(degree)
    # intialized empty array for raw coeffecient
    raw_coef = []
    # continuously loop until the given number of coeffecients 
    # exceeds the number of the given degree by 1
    while not len(raw_coef) == degree + 1:
        # prompt the user to give the number of coeffecients specified in line above
      raw_coef = input("Please enter the coeficiants seperated by spaces: ")
        # and to make sure they are seperated by spaces
      raw_coef = raw_coef.split(" ")
        # convert the every input in the array to floating point numbers
      coef = [float(x) for x in raw_coef]
    # pass those floating point number into the polynomial as coeffecients
    polynomial.setCoef(coef)
    # prompts the user for the given lower bound of the polynomical function
    raw_lower = input("What is the lower bound: ")
    # prompts the user for the given upper bound of the polynomical function
    raw_upper = input("What is the upper bound: ")
    # convert to integers
    lower = int(raw_lower)
    upper = int(raw_upper)
    # initialized variable for method of integration
    method = 0
    # loop until there user enters either 1, 2 or 3 to select integration method
    while not method or method > 3 or method < 0:
        # prompt user of options to integrate
        raw_method = input(
            "Please choose 1. Rectangular, 2. Trapezoid, 3. Exact: ")
        # convert the option to an integer
        method = int(raw_method)
    # if the integration option entered by the user is 1 or 2 and not 3....
    if method != 3:
        #...prompt the user for the number of subdivisions 
        raw_n = input("Please choose n: ")
        n = int(raw_n)
    # integration methods 1 and 2 required a number of subdivisions
    # because rectangle and trapezoidal methods are just approximations
    if method == 1:
        results = RectIntegration.evalLeft(lower, upper, n, polynomial)
    # which involve using subdivisions to evaluate 
    # the approximation of the integral or area under the given polynomial
    elif method == 2:
        results = TrapIntegration.evaluate(lower, upper, n, polynomial)
    # if the user chooses 3, skip asking for the number of subdivisions 
    elif method == 3:
        # because we will not need subdivisions
        #  because this will not be an approximation, 
        # therefore it will be an exact integration,
        # or exact area under the polynomial 
        # between two given points, otherwise known as the lower and upper bounds
        results = ExactIntegration.evaluate(lower, upper, polynomial)
    print(results)
    # continue the while loop for new polynomial functions to integrate
    raw_exit = input("Would you like to do another calculation? y or n?: ")
    # otherwise...
    if raw_exit[0] == 'n' or raw_exit[0] == 'N':
        # end the program
        print("Thank you for choosing the Numerical Integrations Challenge")
        print("Brought to you by AccuWeather!....All Weather, All the Time!!!")
        exit = True