"""
Moduł zawiera podstawowe operacje matematyczne.
"""


def factorial(n):
    """
    Oblicza silnię liczby całkowitej n.

    Args:
        n(int): Liczba nieujemna.

    Returns:
        int: Silnia liczby n.

    Raises:
        ValueError: Jeśli n jest ujemne.
    """
    if n < 0:
        raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych.")
    return 1 if n == 0 else n * factorial(n - 1)


def average(numbers):
    """
    Oblicza średnią arytmetyczną z listy liczb.

    Args:
        numbers(list[float]): Lista liczb.

    Returns:
        float: Średnia wartość.

    Raises:
        ValueError: Jeśli lista jest pusta.
    """
    if not numbers:
        raise ValueError("Lista nie może być pusta!")
    return sum(numbers) / len(numbers)


def median(numbers):
    """
    Oblicza medianę z listy liczb.

    Args:
        numbers(list[float]): Lista liczb.

    Returns:
        float: Mediana.

    Raises:
        ValueError: Jeśli lista jest pusta
    """
    if not numbers:
        raise ValueError("Lista nie może być pusta!")
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_nums[middle - 1] + sorted_nums[middle]) / 2
    else:
        return sorted_nums[middle]
