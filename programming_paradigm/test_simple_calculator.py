
import unittest
from test_simple_calculator import SimpleCalculator
#unittest is a toolbox from Python to write and run tests.
#from simple_calculator import SimpleCalculator means: “bring the calculator we made so we can test it.”

#Make a test class
class TestSimpleCalculator(unittest.TestCase):
#This is a class just like a box to organize tests.
#It must come from unittest.TestCase so Python knows it's a test.    

#Prepare the calculator
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
#This says: Before every test, give me a fresh calculator.
#self.calc is your personal calculator for that test.


#write a test for addition, subtraction, multiplication & Division
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-3, -3), 9)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(5, -1), -5)
        self.assertEqual(self.calc.divide(-8, -2), 4)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
