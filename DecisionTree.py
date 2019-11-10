import Node as nd
import DataSet as ds
import numpy as np


class DecisionTree:

    def __init__(self, file_name):
        self.data_set = None
        self.root = None

        self.create_data_set(file_name)
        self.create_root()

    def create_data_set(self, file_name):
        data = np.loadtxt(file_name, delimiter=',', dtype=str)
        labels = list(ds.DataSet.labels_possible_values.keys())

        self.data_set = ds.DataSet(data, labels)

        self.print()

    def create_root(self):
        self.root = nd.Node(self.data_set)

    def traverse_tree(self):
        print("\n\n   TREE TRAVERSE")
        self.root.traverse()

    def print(self):
        print("\n     CREATING DATA SET")
        print("\n  LABELS")
        print(self.data_set.labels)
        print("\n  DATA")
        print(self.data_set.data)

