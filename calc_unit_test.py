import unittest
import mycalculator as calc
from unittest.mock import patch



class TestCalculatorOperations(unittest.TestCase):
    def setUp(self):
        self.calc = calc.MathOperations()
        self.ui = calc.UserInteractions(self.calc)

    @patch('builtins.input', return_value='5')
    def test_gather_user_input(self, mock_input):
        self.ui.gather_user_input()
        self.assertEqual(self.ui.numbers, [5])

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['a', '1'])
    def test_gather_user_input_invalid(self, mock_input, mock_print):
        self.ui.gather_user_input()
        mock_print.assert_called_with('Invalid Entry')


    @patch('sys.exit', side_effect=SystemExit)    
    @patch('builtins.input', side_effect=['1', '1', '3', '4', '8', '11', 'a', '777', '9',])
    def test_menu(self, mock_input, mock_exit):
        with self.assertRaises(SystemExit):
            self.ui.menu()
        self.assertEqual(self.calc.final_value, 4)

    def test_addition(self):
        self.assertEqual(self.calc.addition([2, 3]), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction([5, 2]), 3)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiplication([4, 3]), 12)

    def test_division(self):
        self.assertEqual(self.calc.division([10, 2]), 5)
        self.assertRaises(ZeroDivisionError, self.calc.division, [10, 0])

    def test_exponents(self):
        self.assertEqual(self.calc.exponents([2, 3]), 8)

    def test_square_value(self):
        self.assertEqual(self.calc.square_value([4]), 16)

    def test_square_root(self):
        self.assertEqual(self.calc.square_root([16]), 4)
        self.assertRaises(ValueError, self.calc.square_root, [-1])


if __name__ == "__main__": #pragma: no cover
    unittest.main()
