import DataSet as ds
import numpy as np
import DecisionTree as dt
import random


class Evaluation:

    def __init__(self, file_name, decision_algorithm, partitioning_method):
        self.data_set = self.create_data_set(file_name)
        self.training_set, self.test_set = self.generate_data_sets(self.data_set, partitioning_method)
        self.decision_tree = dt.DecisionTree(self.training_set, decision_algorithm)
        self.confusion_matrix = None

        self.evaluate()
        self.print_confusion_matrix()

    def create_data_set(self, file_name):  # assuming class is first column and columns separated by ',' commas
        data = np.loadtxt(file_name, delimiter=',', dtype=str)
        labels = list(ds.DataSet.labels_possible_values.keys())

        return ds.DataSet(data, labels)

    def generate_data_sets(self, data_set, partitioning_method=None):
        partitioning_method = 'Holdout' if None else partitioning_method

        if partitioning_method == 'Holdout':
            return self.holdout_partitioning(data_set)
        elif partitioning_method == 'Cross-Validation':
            return self.cross_validation_partitioning(data_set)
        elif partitioning_method == 'Bootstrap':
            return self.bootstrap_partitioning(data_set)

    def evaluate(self):

        confusion_matrix = self.generate_confusion_matrix(self.decision_tree, self.test_set)
        self.confusion_matrix = confusion_matrix

        if confusion_matrix.shape[0] == 2:  # Binary classification

            true_positive = confusion_matrix[0][0]
            true_negative = confusion_matrix[1][1]
            false_positive = confusion_matrix[1][0]
            false_negative = confusion_matrix[0][1]

            num_classified_samples = true_positive + true_negative + false_positive + false_negative

            accuracy = (true_positive + true_negative) / num_classified_samples
            precision = true_positive / (true_positive + false_positive)
            recall = true_positive / (true_positive + false_negative)  # True positive recognition rate
            specificity = true_negative / (true_negative + false_positive)  # True negative recognition rate

            f_measure = 2 * true_positive / (2 * true_positive + false_positive + false_negative)

    def holdout_partitioning(self, data_set, training_set_percentage=None):
        training_set_percentage = 0.66 if training_set_percentage is None else training_set_percentage

        random.shuffle(self.data_set.data)
        num_samples = data_set.data.shape[0]
        num_training_samples = round(num_samples * training_set_percentage)
        training_set = ds.DataSet(self.data_set.data[:num_training_samples], self.data_set.labels)
        test_set = ds.DataSet(self.data_set.data[num_training_samples:], self.data_set.labels)

        return training_set, test_set

    def cross_validation_partitioning(self, data_set):

        return [0], [0]

    def bootstrap_partitioning(self, data_set):

        return [0], [0]

    def generate_confusion_matrix(self, decision_tree, test_set):  # assumes class is first column
        class_values = list(np.unique(self.data_set.data[:, 0]))
        num_classes = len(class_values)
        confusion_matrix = np.zeros((num_classes, num_classes))  # column = true_class, row = training_class

        for sample in test_set.data:
            true_class = sample[0]
            training_class = decision_tree.classify(sample)
            confusion_matrix[class_values.index(training_class)][class_values.index(true_class)] += 1

        return confusion_matrix

    def print_confusion_matrix(self):
        print(self.confusion_matrix)

