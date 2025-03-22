"""
Moduł zawiera funkcje przetwarzające tekst.
"""

import re


def is_palindrome(text):
    """
    Sprawdza czy tekst jest palindromem (ignorując znaki specjalne i wielkość liter).

    Args:
        text(str): Ciąg znaków.

    Returns:
        bool: True jeśli tekst jest palindromem, False w przypadku kiedy nie jest palindromem.
    """
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text.lower())
    return cleaned == cleaned[::-1]


def word_count(text):
    """
    Liczy liczbę słów w tekście.

    Args:
        text(str): Ciąg znaków.

    Returns:
        int: Liczba słów.
    """
    return len(text.split())


def remove_special_characters(text):
    """
    Usuwa znaki specjalne z tekstu.

    Args:
        text(str): Ciąg znaków.

    Returns:
        str: Tekst bez znaków specjalnych.
    """
    return re.sub(r"[^a-zA-Z0-9_ ]", "", text)
