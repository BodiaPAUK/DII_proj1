import unittest
import numpy as np
from Model.defuzzifier import defuzzification

class TestDefuzzification(unittest.TestCase):

    def test_defuzzification_cog(self):
        x = np.array([0, 1, 2, 3, 4])
        mf = np.array([0.0, 0.5, 1.0, 0.5, 0.0])
        result = defuzzification(x, mf, 'cog')
        expected_output = 2.0  # Центр тяжіння симетричної функції
        self.assertAlmostEqual(result, expected_output, places=2)

    def test_defuzzification_fom(self):
        x = np.array([0, 1, 2, 3, 4])
        mf = np.array([0.0, 0.5, 1.0, 0.5, 0.0])
        result = defuzzification(x, mf, 'fom')
        expected_output = 2.0  # Перша максимальна точка
        self.assertEqual(result, expected_output)

    def test_defuzzification_lom(self):
        x = np.array([0, 1, 2, 3, 4])
        mf = np.array([0.0, 0.5, 1.0, 1.0, 0.0])
        result = defuzzification(x, mf, 'lom')
        expected_output = 3.0  # Остання максимальна точка
        self.assertEqual(result, expected_output)

    def test_defuzzification_mom(self):
        x = np.array([0, 1, 2, 3, 4])
        mf = np.array([0.0, 0.5, 1.0, 1.0, 0.0])
        result = defuzzification(x, mf, 'mom')
        expected_output = 2.5  # Середина між 2 і 3 (максимальні значення)
        self.assertEqual(result, expected_output)

    def test_defuzzification_invalid_method(self):
        x = np.array([0, 1, 2, 3, 4])
        mf = np.array([0.0, 0.5, 1.0, 0.5, 0.0])
        result = defuzzification(x, mf, 'non_existent_method')
        self.assertIsNone(result)  # Якщо метод не існує, очікується None

if __name__ == '__main__':
    unittest.main()
