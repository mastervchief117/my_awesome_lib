"""
Moduł zawiera funkcje do przetwarzania danych.
"""


def normalize_list(numbers):
    """
    Normalizuje listę liczb do zakresu 0-1.

    Args:
        numbers(list[float]): Lista liczb.

    Returns:
        list[float]: Lista znormalizowanych wartości.

    Raises:
        ValueError: Jeśli lista jest pusta.
    """
    if not numbers:
        raise ValueError("Lista nie może być pusta!")
    min_val = min(numbers)
    max_val = max(numbers)
    if min_val == max_val:
        return [0.0 for _ in numbers]
    return [(x - min_val) / (max_val - min_val) for x in numbers]


def filter_positive(numbers):
    """
    Zwraca tylko liczby dodatnie z listy.

    Args:
        numbers(list[float]): Lista liczb.

    Returns:
        list[float]: Lista liczb dodatnich.
    """
    return [x for x in numbers if x > 0]


def group_by_type(data_list):
    """
    Grupuje elementy listy według typu danych.

    Args:
        data_list(list): Lista elementów.

    Returns:
        dict: Słownik z nazwami typów jako klucze i listami obiektów jako wartości.
    """
    grouped = {}
    for item in data_list:
        item_type = type(item).__name__
        grouped.setdefault(item_type, []).append(item)
    return grouped
