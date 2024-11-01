import unittest
import numpy as np
from Model.fuzzifier import fuzzification

class TestFuzzification(unittest.TestCase):

    def test_fuzzification_basic(self):
        # Вхідні дані: crisp values та input linguistic variables (input_lvs)
        crisp_values = [5.0]
        input_lvs = [
            {
                'U': np.array([0, 5, 10]),
                'terms': {
                    'Low': np.array([1, 0.5, 0]),
                    'Medium': np.array([0, 0.5, 1]),
                    'High': np.array([0, 0, 1])
                }
            }
        ]
        # Очікуваний результат
        expected_output = {0: {'Low': 0.5, 'Medium': 0.5}}

        # Перевірка результату
        result = fuzzification(crisp_values, input_lvs)
        self.assertEqual(result, expected_output)

    def test_fuzzification_multiple_inputs(self):
        crisp_values = [5.0, 8.0]
        input_lvs = [
            {
                'U': np.array([0, 5, 10]),
                'terms': {
                    'Low': np.array([1, 0.5, 0]),
                    'Medium': np.array([0, 0.5, 1]),
                    'High': np.array([0, 0, 1])
                }
            },
            {
                'U': np.array([0, 5, 10]),
                'terms': {
                    'Cold': np.array([1, 0.5, 0]),
                    'Warm': np.array([0, 0.5, 1]),
                    'Hot': np.array([0, 0, 1])
                }
            }
        ]
        expected_output = {
            0: {'Low': 0.5, 'Medium': 0.5},
            1: {'Warm': 1, 'Hot': 1.0}
        }

        result = fuzzification(crisp_values, input_lvs)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
