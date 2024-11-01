import unittest
import numpy as np
from Model.fuzzy_operators import fuzzy_min, fuzzy_union


class TestFuzzyOperations(unittest.TestCase):

    def test_fuzzy_min_basic(self):
        # Вхідні дані: масив mf та значення value
        mf = np.array([0.2, 0.5, 0.8, 1.0])
        value = 0.6
        # Очікуваний результат
        expected_output = np.array([0.2, 0.5, 0.6, 0.6])

        # Перевірка результату
        np.testing.assert_array_almost_equal(fuzzy_min(mf, value), expected_output)

    def test_fuzzy_union_multiple_mfs(self):
        # Вхідні дані: декілька масивів mf
        mf1 = np.array([0.2, 0.3, 0.7, 0.8])
        mf2 = np.array([0.5, 0.2, 0.6, 0.9])
        mf3 = np.array([0.4, 0.6, 0.5, 0.7])

        # Очікуваний результат
        expected_output = np.array([0.5, 0.6, 0.7, 0.9])

        # Перевірка результату
        np.testing.assert_array_almost_equal(fuzzy_union(mf1, mf2, mf3), expected_output)


if __name__ == '__main__':
    unittest.main()
