import numpy as np


class DataSet():
    # TODO
    labels_possible_values = {} # class variable, added manually?


    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def create_subset(self, class_label, class_value, data=None):
        data = self.data if data is None else data
        column, = np.where(self.labels == class_label)

        if column:
            subset_data = data[data[:, column[0]] == class_value]
            subset_labels = np.delete(self.labels, column[0])

            return DataSet(subset_data, subset_labels)

        return -1
