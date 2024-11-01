import unittest
import numpy as np
from Model.membership_functions import trapmf, trimf

class TestMembershipFunctions(unittest.TestCase):

    def test_trapmf(self):
        x = np.array([0, 2, 4, 6, 8, 10])
        a, b, c, d = 2, 4, 6, 8
        expected_output = np.array([0., 0., 1., 1., 0., 0.])

        np.testing.assert_array_almost_equal(trapmf(x, a, b, c, d), expected_output)

    def test_trapmf_with_boundaries(self):
        x = np.array([2, 4, 6, 8])
        a, b, c, d = 2, 4, 6, 8
        expected_output = np.array([0., 1., 1., 0.])

        np.testing.assert_array_almost_equal(trapmf(x, a, b, c, d), expected_output)

    def test_trapmf_out_of_range(self):
        x = np.array([-2, 0, 10, 12])
        a, b, c, d = 2, 4, 6, 8
        expected_output = np.array([0., 0., 0., 0.])

        np.testing.assert_array_almost_equal(trapmf(x, a, b, c, d), expected_output)

    def test_trmf_basic(self):
        # Вхідні дані: масив x та параметри a, b, c
        x = np.array([1, 3, 5, 7, 9])
        a, b, c = 2, 5, 8
        # Очікуваний результат
        expected_output = np.array([0.0, 0.3333333333333333, 1.0, 0.333333, 0.0])

        # Перевірка на відповідність
        np.testing.assert_array_almost_equal(trimf(x, a, b, c), expected_output)

    def test_trimf_out_of_range(self):
        x = np.array([-1, 0, 10, 12])
        a, b, c = 2, 5, 8
        expected_output = np.array([0.0, 0.0, 0.0, 0.0])

        # Перевірка на відповідність для значень поза діапазоном
        np.testing.assert_array_almost_equal(trimf(x, a, b, c), expected_output)

    def test_trimf_single_value_array(self):
        # Тест з одним значенням, що потрапляє в пікову точку
        x = np.array([5])  # Очікується пік функції при x == b
        a, b, c = 2, 5, 8
        expected_output = np.array([1.0])

        np.testing.assert_array_almost_equal(trimf(x, a, b, c), expected_output)


if __name__ == '__main__':
    unittest.main()
