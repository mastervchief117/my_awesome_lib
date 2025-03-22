import unittest
from data_utils import normalize_list, filter_positive, group_by_type


class TestDataUtils(unittest.TestCase):

    def test_normalize_list(self):
        self.assertEqual(normalize_list([1, 2, 3]), [0.0, 0.5, 1.0])  # przypadek typowy
        self.assertEqual(normalize_list([5, 5, 5]), [0.0, 0.0, 0.0])
        with self.assertRaises(ValueError):
            normalize_list([])  # pusta lista

    def test_filter_positive(self):
        self.assertEqual(filter_positive([1, -1, 0, 3]), [1, 3])  # mieszane
        self.assertEqual(filter_positive([-5, -2]), [])  # ujemne
        self.assertEqual(filter_positive([0]), [])  # tylko 0

    def test_group_by_type(self):
        data = [1, "a", 2.5, "b", True, 3]
        result = group_by_type(data)
        self.assertEqual(result["int"], [1, 3])
        self.assertEqual(result["str"], ["a", "b"])
        self.assertEqual(result["float"], [2.5])
        self.assertEqual(result["bool"], [True])


if __name__ == "__main__":
    unittest.main()
