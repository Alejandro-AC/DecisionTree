import unittest
import DataSet as ds
import numpy as np


class Testing(unittest.TestCase):

    def test_subset(self):
        print("TEST - DataSet - Creating Subset")
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
        print('\n DATASET')
        print(data_set_1)

        print('\n LABELS')
        data_labels_1 = ['PlayTennis', 'Outlook', 'Temperature', 'Humidity', 'Wind']
        print(data_labels_1)

        dataset = ds.DataSet(data_set_1, data_labels_1)

        print('\n TEST CASE 1')
        print('\n Class: Outlook')
        print(' Value: Sunny')
        print('\n\n RESULT SUBSET')
        result = dataset.create_subset('Outlook', 'Sunny')
        print(result.data)
        print('\n RESULT LABELS')
        print(result.labels)

        expected_labels = ['PlayTennis', 'Temperature', 'Humidity', 'Wind']
        expected_data = [['No', 'Hot', 'High', 'Weak'],
                         ['No', 'Hot', 'High', 'Strong'],
                         ['No', 'Mild', 'High', 'Weak'],
                         ['Yes', 'Cool', 'Normal', 'Weak'],
                         ['Yes', 'Mild', 'Normal', 'Strong']
                         ]

        np.testing.assert_array_equal(expected_labels, result.labels)
        np.testing.assert_array_equal(expected_data, result.data)

        print('\n TEST CASE 2')
        print('\n Class: Humidity')
        print(' Value: High')
        print('\n\n RESULT SUBSET')
        result = dataset.create_subset('Humidity', 'High')
        print(result.data)
        print('\n RESULT LABELS')
        print(result.labels)

        expected_labels = ['PlayTennis', 'Outlook', 'Temperature', 'Wind']
        expected_data = [['No', 'Sunny', 'Hot', 'Weak'],
                         ['No', 'Sunny', 'Hot', 'Strong'],
                         ['Yes', 'Overcast', 'Hot', 'Weak'],
                         ['Yes', 'Rain', 'Mild', 'Weak'],
                         ['No', 'Sunny', 'Mild', 'Weak'],
                         ['Yes', 'Overcast', 'Mild', 'Strong'],
                         ['No', 'Rain', 'Mild', 'Strong']
                         ]

        np.testing.assert_array_equal(expected_labels, result.labels)
        np.testing.assert_array_equal(expected_data, result.data)

        print('\n TEST CASE 3')
        print('\n Class: Wind')
        print(' Value: NonExistant Value')
        print('\n\n RESULT SUBSET')
        result = dataset.create_subset('Wind', 'NonExistant')
        print(result.data)
        print('\n RESULT LABELS')
        print(result.labels)

        expected_labels = ['PlayTennis', 'Outlook', 'Temperature', 'Humidity']
        expected_data = np.array([])

        np.testing.assert_array_equal(expected_labels, result.labels)
        self.assertEquals(expected_data.size, 0)

        print('\n TEST CASE 4')
        print('\n Class: NonExistant Class')
        print(' Value: N/A')
        print('\n\n RESULT SUBSET')
        with self.assertRaises(ValueError):
            dataset.create_subset('N/A', 'N/A')


if __name__ == '__main__':
    unittest.main()
