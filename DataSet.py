import numpy as np


class DataSet:
    # TODO
    labels_possible_values = {}  # class variable, added manually?
    labels_possible_values_list = [] # class variable, added manually?
    missing_value_indicator = None

    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def create_subset(self, class_label, class_value, data=None):
        data = self.data if data is None else data
        column = self.labels.index(class_label)

        if column:
            subset_data = data[data[:, column] == class_value]
            subset_labels = self.labels[:column] + self.labels[column + 1:]
            subset_data = np.delete(subset_data, column, 1)

            return DataSet(subset_data, subset_labels)

        print(' ERROR creating SubSet')
        return -1

    def remove_lines_with_missing_values(self):
        self.data = self.data[np.all(self.data != DataSet.missing_value_indicator, axis=1)]
