import DecisionAlgorithm as da
import DataSet as ds
import numpy as np


class Node:

    def __init__(self, data_set, class_label=None, class_value=None):
        self.children_list = []
        self.data_set = data_set
        self.class_label = class_label
        self.class_value = class_value

        self.decision_algorithm = da.DecisionAlgorithm('ID3', self.data_set.data)  # TODO make it class/global variable of the Tree

        # Check that there is more than 1 column (+ Class) and that Class has different values
        if self.data_set.data.shape[1] > 2 and len(np.unique(self.data_set.data[:, 0])) > 1:
            self.create_children()

    def create_children(self):
        class_label_idx = self.decision_algorithm.decide_class()
        class_label = self.data_set.labels[class_label_idx]

        for class_value in ds.DataSet.labels_possible_values[class_label]:
            child_subset = self.data_set.create_subset(class_label, class_value)
            child = Node(child_subset, class_label, class_value)
            self.children_list.append(child)

    def traverse(self, depth=0):
        print('\n')
        print("".rjust(depth * 3, '-') + " Node Class: " + str(self.class_label))
        print("".rjust(depth * 3, ' ') + " Node Value: " + str(self.class_value))
        print("".rjust(depth * 3, '-') + " Node Depth: " + str(depth))
        for child in self.children_list:
            child.traverse(depth + 1)

