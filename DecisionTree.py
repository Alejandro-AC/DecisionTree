import Node as nd
import DataSet as ds
import DecisionAlgorithm as da
import numpy as np
from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


class DecisionTree:

    def __init__(self, data_set, decision_algorithm):
        self.data_set = data_set
        self.decision_algorithm = da.DecisionAlgorithm(algorithm=decision_algorithm)
        self.root = nd.Node(self.data_set, self.decision_algorithm)

    def classify(self, sample):
        node = self.root

        while node and node.children_list:
            attribute_used_to_decide = node.attribute_label
            attribute_idx = np.where(ds.DataSet.labels_possible_values_list[:, 0] == attribute_used_to_decide)[0][0]
            attribute_value = sample[attribute_idx]

            child = node.get_child_by_attribute_value(attribute_value)

            if child.num_samples == 0:
                return node.get_most_common_class()

            if not child.children_list:
                return child.get_most_common_class()

            node = child

        print('ERROR in classify - Unexpected code reached')
        return -1

    def traverse_tree(self):
        print("\n\n   TREE TRAVERSE")
        g = Digraph('DecisionTree', format='png', filename='decisionTree.gv')
        g.attr('node', shape='box')

        self.root.traverse(g)

        g.render(view=True)

    def print(self):
        print("\n     CREATING DATA SET")
        print("\n  LABELS")
        print(self.data_set.labels)
        print("\n  DATA")
        print(self.data_set.data)

