import unittest
import DataSet as ds
import Node as nd
import numpy as np
from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


class Testing(unittest.TestCase):

    def test_traverse(self):
        print("\n\nTEST - DataSet - Creating Subset")
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
        data_labels_1 = ['class', 'Outlook', 'Temperature', 'Humidity', 'Wind']
        print(data_labels_1)

        dataset = ds.DataSet(data_set_1, data_labels_1)
        ds.DataSet.labels_possible_values = {'class': ['Yes', 'No'],
                                             'Outlook': ['Sunny', 'Overcast', 'Rain'],
                                             'Temperature': ['Hot', 'Mild', 'Cool'],
                                             'Humidity': ['High', 'Normal'],
                                             'Wind': ['Weak', 'Strong']
                                             }
        node = nd.Node(dataset)

        print('\n TEST CASE 1')
        node.create_children()

        g = Digraph('DecisionTree', format='png', filename='test-output/decisionTree.gv')
        g.attr('node', shape='box')

        node.traverse(g, 0)

        g.render()


if __name__ == '__main__':
    unittest.main()
