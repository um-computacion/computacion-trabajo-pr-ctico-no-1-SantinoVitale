import unittest
from src.roman_converter import decimal_to_roman 
# Va a fallar porque no existe el archivo aún con la funcion decimal_to_roman


class TestRomanConverter(unittest.TestCase):
    def test_general(self):
        self.assertRaises(TypeError, decimal_to_roman, "abc")
        self.assertRaises(TypeError, decimal_to_roman, 3.14)
        self.assertRaises(TypeError, decimal_to_roman, None)
        self.assertRaises(ValueError, decimal_to_roman, 0)
        self.assertRaises(ValueError, decimal_to_roman, -1)
        self.assertRaises(ValueError, decimal_to_roman, 4000)

    def test_basic_numbers(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(10), "X")
        self.assertEqual(decimal_to_roman(50), "L")
        self.assertEqual(decimal_to_roman(100), "C")
        self.assertEqual(decimal_to_roman(500), "D")
        self.assertEqual(decimal_to_roman(1000), "M")

    def test_subtraction_rules(self):
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(90), "XC")
        self.assertEqual(decimal_to_roman(400), "CD")
        self.assertEqual(decimal_to_roman(900), "CM")

    def test_complex_numbers(self):
        self.assertEqual(decimal_to_roman(49), "XLIX")
        self.assertEqual(decimal_to_roman(99), "XCIX")
        self.assertEqual(decimal_to_roman(499), "CDXCIX")
        self.assertEqual(decimal_to_roman(999), "CMXCIX")
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

if __name__ == '__main__':
    unittest.main()