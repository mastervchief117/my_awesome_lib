# My Awesome Library

**My Awesome Library** to prosta biblioteka Pythona, która zawiera zestaw narzędzi przydatnych do:
- Obliczeń matematycznych
- Przetwarzania tekstu
- Operacji na danych (listach)

Może być przydatna do nauki, testów jednostkowych i codziennego użytku w małych projektach.

## Instalacja

Jeżeli masz repozytorium lokalnie, wpisz w terminalu:

```bash
pip install -e .
```

Możesz też po prostu skopiować folder `my_awesome_lib` do swojego projektu i zaimportować potrzebne moduły.

## Przykłady wywołań

### Moduł `math_tools`

```python
from math_tools import factorial, average, median

print(factorial(5))  # 120
print(average([1, 2, 3]))  # 2.0
print(median([1, 2, 3, 4]))  # 2.5
```

### Moduł `data_utils`

```python
from data_utils import normalize_list, filter_positive, group_by_type

print(normalize_list([0, 5, 10]))  # [0.0, 0.5, 1.0]
print(filter_positive([-2, 0, 3, 4]))  # [3, 4]
print(group_by_type([1, "a", 2.5]))  # {'int': [1], 'str': ['a'], 'float': [2.5]}
```

### Moduł `text_processing`

```python
from text_processing import is_palindrome, word_count, remove_special_characters

print(is_palindrome("Kajak"))  # True
print(word_count("To jest przykładowy tekst"))  # 4
print(remove_special_characters("Hello!@#"))  # "Hello"
```

## Wersja

1.0.0

## Autor

Patrycja Dorszyńska

## Licencja

Projekt dostępny na licencji MIT. Możesz go dowolnie modyfikować, kopiować i rozpowszechniać z zachowaniem oryginalnej licencji.
