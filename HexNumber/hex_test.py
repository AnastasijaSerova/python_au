import unittest
from hex_number import HexNumber


class Test_HexNumber(unittest.TestCase):

    def test_add1(self):
        num1 = HexNumber('1111')
        num2 = HexNumber('2222')
        self.assertEqual(str(num1 + num2), '3333')

    def test_add2(self):
        num1 = HexNumber('8AB')
        num2 = HexNumber('B78')
        self.assertEqual(str(num1 + num2), '1423')

    def test_add3(self):
        num1 = HexNumber('FFA1')
        num2 = HexNumber('154A')
        self.assertEqual(str(num1 + num2), '114EB')


if __name__ == '__main__':
    unittest.main()
