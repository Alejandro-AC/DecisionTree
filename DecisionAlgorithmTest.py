import unittest
import DecisionAlgorithm as da
import numpy as np


class Testing(unittest.TestCase):

    def test_entropy_shannon(self):
        decision_algorithm_id3 = da.DecisionAlgorithm('id3', None)
        values_1 = ['e', 'e', 'e', 'e', 'e', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f']

        expected = 0.94
        test_subject = decision_algorithm_id3.calculate_entropy(values_1)

        self.assertAlmostEqual(expected, test_subject, places=2)

    def test_gain_list(self):
        data_set_1 = np.array([['No', 'Sunny', 'Hot', 'High', 'Weak'],
                               ['No', 'Sunny', 'Hot', 'High', 'Strong'],
                               ['Yes', 'Overcast', 'Hot', 'High', 'Weak'],
                               ['Yes', 'Rain', 'Mild', 'High', 'Weak'],
                               ['Yes', 'Rain', 'Cool', 'Normal', 'Weak'],
                               ['No', 'Rain', 'Cool', 'Normal', 'Strong'],
                               ['Yes', 'Overcast', 'Cool', 'Normal', 'Strong'],
                               ['No', 'Sunny', 'Mild', 'High', 'Weak'],
                               ['Yes', 'Sunny', 'Cool', 'Normal', 'Weak'],
                               ['Yes', 'Rain', 'Mild', 'Normal', 'Weak'],
                               ['Yes', 'Sunny', 'Mild', 'Normal', 'Strong'],
                               ['Yes', 'Overcast', 'Mild', 'High', 'Strong'],
                               ['Yes', 'Overcast', 'Hot', 'Normal', 'Weak'],
                               ['No', 'Rain', 'Mild', 'High', 'Strong']
                               ])

        decision_algorithm_id3 = da.DecisionAlgorithm('id3', data_set_1)

        expected = [0.9402859586706309, 0.24674981977443888, 0.029222565658954647, 0.15183550136234142,
                    0.04812703040826927]
        test_entropy = decision_algorithm_id3.calculate_entropy()
        test_subject = decision_algorithm_id3.calculate_gain(test_entropy)

        self.assertAlmostEqual(expected, test_subject)


if __name__ == '__main__':
    unittest.main()
