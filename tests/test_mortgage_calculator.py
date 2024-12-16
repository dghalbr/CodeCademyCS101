import unittest
from unittest.mock import patch
import sys
import os

# Add the path to the mortgage_calculator module
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../mortgage-calculator'))
sys.path.insert(0, module_path)

# Check if the module file exists
if not os.path.exists(os.path.join(module_path, 'mortgage_calculator.py')):
    raise ModuleNotFoundError("Module mortgage_calculator not found. Please check the module name and path.")

from mortgage_calculator import get_user_input, calculate_monthly_payment


# patch isn't working for some reason. these look correct but wont mock the input for the tests
class TestMortgageCalculator(unittest.TestCase):

    @patch('builtins.input', side_effect=[100000, 5, 30])
    def test_get_user_input(self, mock_input):
        principal, annual_interest_rate, years = get_user_input()
        self.assertEqual(principal, 100000)
        self.assertEqual(annual_interest_rate, 5)
        self.assertEqual(years, 30)

    @patch('builtins.input', side_effect=[100000, 5, 30])
    def test_calculate_monthly_payment(self, mock_input):
        principal = 100000
        annual_interest_rate = 5
        years = 30
        expected_payment = 536.82
        result = calculate_monthly_payment(principal, annual_interest_rate, years)
        self.assertAlmostEqual(result, expected_payment, places=2)

if __name__ == '__main__':
    unittest.main()
