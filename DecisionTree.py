import Node as nd
import DataSet as ds
import DecisionAlgorithm as da
import numpy as np
from graphviz import Digraph
import datetime
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


class DecisionTree:

    def __init__(self, data_set, decision_algorithm):
        self.data_set = data_set
        self.decision_algorithm = da.DecisionAlgorithm(algorithm=decision_algorithm)
        self.root = nd.Node(self.data_set, self.decision_algorithm)

    def classify(self, sample, node=None):
        node = self.root if node is None else node

        while node and node.children_list:
            attribute_used_to_decide = node.attribute_label
            attribute_idx = np.where(ds.DataSet.labels_possible_values_list[:, 0] == attribute_used_to_decide)[0][0]
            attribute_value = sample[attribute_idx]

            if attribute_value == ds.DataSet.missing_value_indicator:
                return node.class_values[np.argmax(self.get_class_by(node, sample))]

            child = node.get_child_by_attribute_value(attribute_value)

            if child.num_samples == 0:
                return node.get_most_common_class()

            node = child

        if not node.children_list:
            return node.get_most_common_class()

        print('ERROR in classify - Unexpected code reached')
        return -1

    def get_class_by(self, node, sample):

        for child in node.children_list:
            if not child.children_list or not child.num_samples == 0:
                return child.class_counts / node.num_samples

            elif child.attribute_value == ds.DataSet.missing_value_indicator:
                return child.class_counts / node.num_samples * self.get_class_by(child, sample)

            else:
                return child.class_counts / node.num_samples

        class_counts = [0] * len(ds.DataSet.labels_possible_values_list[0][0])
        return np.add(class_counts, self.get_class_by())

    def traverse_tree(self):
        filename = 'decisionTree_' + str(datetime.datetime.now()) + '.gv'
        g = Digraph('DecisionTree', format='png', filename=filename.replace(' ', '').replace(':', '-'))
        g.attr('node', shape='box')

        self.root.traverse(g)

        g.render(view=True)

    def print(self):
        print("\n     CREATING DATA SET")
        print("\n  LABELS")
        print(self.data_set.labels)
        print("\n  DATA")
        print(self.data_set.data)
