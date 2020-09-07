import unittest

class Polynomial(object):
  def __init__(self, degree):
    self.degree = degree
    self.coef = []
    
  def setCoef(self, coef):
    if len(coef) == self.degree+1:
      self.coef = coef
      
  def evaluate(self, x):
    result = 0
    degree = self.degree
    while not degree < 0:
      result += (x**degree)*self.coef[degree]
      degree -= 1
    return result
  
  def find_anti(self):
    degree = self.degree+1
    anti_derivative = Polynomial(degree)
    counter = 0
    new_coef = []
    while not degree == 0:
      new_coef.append(self.coef[counter]/degree)
      degree -= 1
      counter += 1
    new_coef.append(0)
    anti_derivative.setCoef(new_coef)
    return anti_derivative

if __name__ == '__main__':
    class TestPolynomial(unittest.TestCase):
        def test_degree(self):
            poly = Polynomial(2)
            self.assertEqual(poly.degree, 2)

        def test_coef(self):
            poly = Polynomial(2)
            poly.setCoef([1, 2, 1])
            self.assertEqual(poly.coef, [1, 2, 1])

        def test_eval(self):
            poly = Polynomial(2)
            poly.setCoef([1, 2, 1])
            self.assertEqual(poly.evaluate(2), 9)

        def test_anti(self):
            poly = Polynomial(2)
            poly.setCoef([1, 2, 1])
            anti = Polynomial(3)
            anti.setCoef([1/3, 1, 1, 0])
            self.assertEqual(poly.find_anti().coef, anti.coef)
            
    unittest.main()