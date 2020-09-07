#!/usr/bin/python3

from polynomial import Polynomial
import unittest

class RectIntegration(object):
  @staticmethod
  def findDeltaX(a,b,n):
    return (b-a)/n

  @classmethod
  def evalLeft(cls, lower, upper, n, poly):
    delta_x = cls.findDeltaX(lower, upper, n)
    xs = [lower+i*delta_x for i in range(n)]
    fx = [poly.evaluate(x) for x in xs]
    return delta_x*sum(fx)

  @classmethod
  def evalRight(cls, lower, upper, n, poly):
    delta_x = cls.findDeltaX(lower, upper, n)
    xs = [lower+(i+1)*delta_x for i in range(n)]
    print(xs)
    fx = [poly.evaluate(x) for x in xs]
    print()
    return delta_x*sum(fx)

class TrapIntegration(object):
  @staticmethod
  def evaluate(lower, upper, n, poly):
    return .5 *(RectIntegration.evalLeft(lower, upper, n, poly) + 
                RectIntegration.evalRight(lower, upper, n, poly))

class ExactIntegration(object):
  @staticmethod
  def evaluate(lower, upper, poly):
    anti_deriv = poly.find_anti()
    return anti_deriv.evaluate(upper) - anti_deriv.evaluate(lower)

if __name__ == '__main__':
    class TestPolynomial(unittest.TestCase):
        def setUp(self):
            self.poly = Polynomial(2)
            self.poly.setCoef([1., 2., 1.])

        def test_evalLeft(self):
            self.assertTrue(abs(RectIntegration.evalLeft(0, 1, 2, self.poly) 
                                     - 1.625) < .5)

        def test_evalRight(self):
            self.assertTrue(abs(RectIntegration.evalRight(0, 1, 2, self.poly) 
                                     - 3.125) < .5)
        def test_evalTrap(self):
            self.assertTrue(abs(TrapIntegration.evaluate(0, 1, 2, self.poly) 
                                     - 2.375) < .5)

        def test_evalExact(self):
            self.assertTrue(abs(ExactIntegration.evaluate(0, 1, self.poly) 
                                     - 2.333) < .5)
            
    unittest.main()