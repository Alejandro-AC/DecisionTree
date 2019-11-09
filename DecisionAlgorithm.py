import numpy as np
import math
from math import log, e
from collections import Counter


class DecisionAlgorithm():

    def __init__(self, algorithm, data_set):
        self.algorithm = algorithm
        self.data_set = data_set

    def decide_class(self, algorithm=None, data_set=None):
        algorithm = self.algorithm if algorithm is None else algorithm
        data_set = self.data_set if data_set is None else data_set

        if algorithm is 'ID3':
            return self.decide_id3(data_set)
        else:
            return -1

    def decide_id3(self, data_set):
        base_entropy = self.calculate_entropy(data_set[:, 0], 0)

        attribute_gain_list = self.calculate_gain(base_entropy, data_set)
        max_gain_attribute_idx = np.argmax(attribute_gain_list[1:])

        return max_gain_attribute_idx

    def calculate_entropy(self, class_values=None, base=None):
        class_values = self.data_set[:,0] if class_values is None else class_values
        # base Shannon as default
        base = 2 if base is None else base

        value, counts = np.unique(class_values, return_counts=True)
        norm_counts = counts / counts.sum()

        return -(norm_counts * np.log(norm_counts) / np.log(base)).sum()

    def calculate_gain(self, base_entropy=None, data_set=None):
        data_set = self.data_set if data_set is None else data_set

        num_columns = data_set.shape[1]
        gain_list = [base_entropy] * num_columns  # Initialize with base value
        for col in range(1, num_columns):
            unique_values, counts = np.unique(data_set[:, col], return_counts=True)
            total_count = counts.sum()
            reduced_matrix = data_set[:, [0, col]]  # Matrix with only class and current columns
            for value, count in zip(unique_values, counts):
                value_rows = reduced_matrix[np.where(reduced_matrix[:, 1] == value)]  # Matrix of rows with current value
                gain_list[col] -= count / total_count * self.calculate_entropy(value_rows[:, 0], 2)

        return gain_list
