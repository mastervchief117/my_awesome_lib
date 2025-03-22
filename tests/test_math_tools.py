import unittest
from math_tools import factorial, average, median


class TestMathTools(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)  # przypadek brzegowy
        self.assertEqual(factorial(5), 120)  # przypadek typowy
        with self.assertRaises(ValueError):
            factorial(-3)  # przypadek błędny

    def test_average(self):
        self.assertEqual(average([1, 2, 3]), 2.0)  # przypadek typowy
        self.assertEqual(average([5]), 5.0)  # przypadek brzegowy (1 element)
        with self.assertRaises(ValueError):
            average([])  # przypadek błędny (pusta lista)

    def test_median(self):
        self.assertEqual(median([1, 2, 3]), 2)  # nieparzysta liczba elementów
        self.assertEqual(median([1, 2, 3, 4]), 2.5)  # parzysta liczba elementów
        with self.assertRaises(ValueError):
            median([])  # przypadek błędny (pusta lista)


if __name__ == "__main__":
    unittest.main()
