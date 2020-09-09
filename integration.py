#!/usr/bin/python3

from polynomial import Polynomial
import unittest

class RectIntegration(object):
  # Computes the width of the rectangles
  @staticmethod
  # find delta_x 
  def findDeltaX(a,b,n):
    # return the difference of the lower and upper bound 
    # divided by the number od subdivisions
    return (b-a)/n

  # Approximates the integral of a polynomial using left riemann sum
  @classmethod
  # this method left approximates the integral of the polynomial 
  # given the lower and upper bound 
  # and the number of subdivisions
  def evalLeft(cls, lower, upper, n, poly):
    # delta_x equals the upper bound minus the lower bound 
    # divided by the number of subdivions
    delta_x = cls.findDeltaX(lower, upper, n)
    # Left Riemann Sum Formula, L = delta_x( f(x_0) + f(x_1) +....+ f(x_n-1)
    xs = [lower+i*delta_x for i in range(n)]
    # each f(x) evaluated at every point x marked by the subdivsions
    fx = [poly.evaluate(x) for x in xs]
    # return delta_x times the sum of f(x)
    return delta_x*sum(fx)

  # Approximates the integral of a polynomial using right riemann sum
  @classmethod
  # this method right approximates the integral of the polynomial 
  # given the lower and upper bounds
  # and the number of subdivisions
  def evalRight(cls, lower, upper, n, poly):
    # delta_x equals the upper bound minus the lower bound 
    # divided by the number of subdivions
    delta_x = cls.findDeltaX(lower, upper, n)
    # Right Riemann Sum Formula, R = deltax( f(x0) + f(x1) +....+ f(xn)
    xs = [lower+(i+1)*delta_x for i in range(n)]
    # each f(x) evaluated at every point x marked by the subdivsions
    fx = [poly.evaluate(x) for x in xs]
    # return delta_x times the sum of f(x)
    return delta_x*sum(fx)

# Computes the integral of a polynomial using trapezoidal integration
class TrapIntegration(object):
  @staticmethod
  # this method approximates the integral of the polynomial 
  # given the lower and upper bounds 
  # and the number of subdivisions
  def evaluate(lower, upper, n, poly):
    # return 1/2 multiplied by 
    # the sum of Right Riemann Sum 
    # and Left Riemann Sum of the polynomial
    # (L + R) / 2
    return .5 *(RectIntegration.evalLeft(lower, upper, n, poly) + 
                RectIntegration.evalRight(lower, upper, n, poly))
# Computes the exact integral of a polynomial
class ExactIntegration(object):
  @staticmethod
  # this method evaluates the exact integral of the polynomial 
  # given the lower and upper bounds
  def evaluate(lower, upper, poly):
    # antiderivative or indefinite integral of the polynomial
    anti_deriv = poly.find_anti()
    # return the antiderivative evaluated at the upper bound 
    # minus 
    # the antiderivative evaluated at the lower bound
    return anti_deriv.evaluate(upper) - anti_deriv.evaluate(lower)

if __name__ == '__main__':
    # Test Class that runs integrations and return an output
    class TestPolynomial(unittest.TestCase):
        # Set up is called before each test and then 
        def setUp(self):
            self.poly = Polynomial(2)
            self.poly.setCoef([1., 2., 1.])
        # Tests whether the integral of a polynomial is computed 
        # using left rectangular integration
        def test_evalLeft(self):
            self.assertTrue(abs(RectIntegration.evalLeft(0, 1, 2, self.poly) 
                                     - 1.625) < .5)
        # Tests whether the integral of a polynomial is computed 
        # using right rectangular integration
        def test_evalRight(self):
            self.assertTrue(abs(RectIntegration.evalRight(0, 1, 2, self.poly) 
                                     - 3.125) < .5)
        # Tests whether the integral of a polynomial is computed 
        # using trapezoidal integration
        def test_evalTrap(self):
            self.assertTrue(abs(TrapIntegration.evaluate(0, 1, 2, self.poly) 
                                     - 2.375) < .5)
        
        # Tests whether the integral of a polynomial is computed 
        # using exact integration
        def test_evalExact(self):
            self.assertTrue(abs(ExactIntegration.evaluate(0, 1, self.poly) 
                                     - 2.333) < .5)
            
    unittest.main()