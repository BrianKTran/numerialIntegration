#!/usr/bin/python3

import unittest

class Polynomial(object):
  # Constructor where the object
  # is the degree of a given polynomial
  def __init__(self, degree):
    self.degree = degree
    self.coef = []
  # Constructor where the object is 
  # are the coefficients of a given polynomial
  def setCoef(self, coef):
    # the number of coeffecients is one more than the degree number
    if len(coef) == self.degree+1:
      self.coef = coef
  
  # method for evaluating x to the degreeth power times the degree of the last given coeffecient
  def evaluate(self, x):
    result = 0
    degree = self.degree
    # while the degree is not less than 0
    while not degree < 0:
    # result is x to the given degree'th power times the given degree of the last given coeffecient
      result += (x**degree)*self.coef[degree]
    # the degrees in a polynomial function decrement by 1
      degree -= 1
    # return x^given degree'th power times the given coeffecient
    return result
  
  # method for evaluating the antiderivative of a polynomial function
  def find_anti(self):
    # variable set to one more than the degree 
    degree = self.degree+1
    # variable set to the polynomical function 
    # with given object degree passed in
    anti_derivative = Polynomial(degree)
    # initialized counter at 0
    counter = 0
    # initialized variable for new coeffecient at empty array
    new_coef = []
    # while the degree is not 0
    while not degree == 0:
    # add the last given coeffeciecnt divided by the given degree
    # to the empty array as new coeffecient
      new_coef.append(self.coef[counter]/degree)
      # degrees decrement by 1 in a polynomial function
      degree -= 1
      # counter increments by 1 for the last coeffecient
      counter += 1
    # adding 0 to the array- new coeffecient - 
    new_coef.append(0)
    # pass the new coeffecient to the polynomial function
    anti_derivative.setCoef(new_coef)
    # return the antiderivative
    return anti_derivative

if __name__ == '__main__':
    class TestPolynomial(unittest.TestCase):
        # test different degrees method
        def test_degree(self):
            poly = Polynomial(2)
            self.assertEqual(poly.degree, 2)

        # test different coeffecients method
        def test_coef(self):
            poly = Polynomial(2)
            poly.setCoef([1, 2, 1])
            self.assertEqual(poly.coef, [1, 2, 1])

        # test evaluation method
        def test_eval(self):
            poly = Polynomial(2)
            poly.setCoef([1, 2, 1])
            self.assertEqual(poly.evaluate(2), 9)
        # test anti_derivative method
        def test_anti(self):
            poly = Polynomial(2)
            poly.setCoef([1, 2, 1])
            anti = Polynomial(3)
            anti.setCoef([1/3, 1, 1, 0])
            self.assertEqual(poly.find_anti().coef, anti.coef, poly.find_anti().degree)
            
    unittest.main()