import unittest
import main


class TestAddition(unittest.TestCase):
    def test_addition(self):
        num1 = num2 = 5
        result = main.add_two_number(num1,num2)
        self.assertEqual(result,10)


unittest.main()