import numpy as np


class DataSet():
    # TODO
    labels_possible_values = {}  # class variable, added manually?

    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def create_subset(self, class_label, class_value, data=None):
        data = self.data if data is None else data
        column = self.labels.index(class_label)

        if column:
            subset_data = data[data[:, column] == class_value]
            subset_labels = self.labels[:column] + self.labels[column + 1:]

            return DataSet(subset_data, subset_labels)

        print('ERROR creating Sub set')
        return -1
