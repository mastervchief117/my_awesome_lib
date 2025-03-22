import unittest
from text_processing import is_palindrome, word_count, remove_special_characters


class TestTextProcessing(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Kajak"))  # przypadek typowy
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama!"))  # zdanie
        self.assertFalse(is_palindrome("Python"))  # nie palindrom

    def test_word_count(self):
        self.assertEqual(word_count("To jest test"), 3)  # przypadek typowy
        self.assertEqual(word_count("Jedno"), 1)  # przypadek brzegowy
        self.assertEqual(word_count(""), 0)  # pusty tekst

    def test_remove_special_characters(self):
        self.assertEqual(
            remove_special_characters("Hello!@# World..."), "Hello World"
        )  # przypadek typowy
        self.assertEqual(
            remove_special_characters("123_ABC*&%$"), "123_ABC"
        )  # zaqchowanie podkreślnika
        self.assertEqual(remove_special_characters("?!#"), "")  # tylko znaki specjalne


if __name__ == "__main__":
    unittest.main()
