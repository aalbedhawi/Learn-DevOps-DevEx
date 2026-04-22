import unittest
import mycalculator

class TestCalculatorOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(mycalculator.MathOperations().addition([2, 3]), 5 )

    def test_subtraction(self):
        self.assertEqual(mycalculator.MathOperations().subtraction([5, 2]), 3)

    def test_multiplication(self):
        self.assertEqual(mycalculator.MathOperations().multiplication([4, 3]), 12)

# TODO: division needs an additional test for dividion by zero
    def test_division(self):
        self.assertEqual(mycalculator.MathOperations().division([10, 2]), 5)

if __name__ == '__main__':
    unittest.main()