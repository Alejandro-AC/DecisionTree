import DataSet as ds
import numpy as np
import DecisionTree as dt


class Evaluation:

    def __init__(self, file_name, decision_algorithm, partitioning_method):

        self.data_set = self.create_data_set(file_name)
        self.decision_algorithm = decision_algorithm
        self.partitioning_method = partitioning_method
        self.confusion_matrix = None

        self.evaluate()

    def create_data_set(self, file_name):  # assuming class is first column and columns separated by ',' commas
        data = np.loadtxt(file_name, delimiter=',', dtype=str)
        labels = list(ds.DataSet.labels_possible_values.keys())
        data_set = ds.DataSet(data, labels)
        data_set.remove_lines_with_missing_values()

        return data_set

    def evaluate(self):
        if self.partitioning_method == 'Holdout':
            self.holdout_partitioning(self.data_set, self.decision_algorithm)
        elif self.partitioning_method == 'Cross-Validation':
            self.cross_validation_partitioning(self.data_set, self.decision_algorithm)
        elif self.partitioning_method == 'Bootstrap':
            self.bootstrap_partitioning(self.data_set, self.decision_algorithm)

        self.print_confusion_matrix()
        self.print_metrics()

    def holdout_partitioning(self, data_set, decision_algorithm, training_set_percentage=None):
        training_set_percentage = 0.66 if training_set_percentage is None else training_set_percentage

        np.random.shuffle(data_set.data)

        num_samples = data_set.data.shape[0]
        num_training_samples = round(num_samples * training_set_percentage)
        training_set = ds.DataSet(data_set.data[:num_training_samples], data_set.labels)
        test_set = ds.DataSet(data_set.data[num_training_samples:], data_set.labels)

        d_tree = dt.DecisionTree(training_set, decision_algorithm)

        self.confusion_matrix = self.generate_confusion_matrix(d_tree, test_set)

    def cross_validation_partitioning(self, data_set):

        return [0], [0]

    def bootstrap_partitioning(self, data_set, decision_algorithm, k=None, training_set_percentage=None):
        k = 42 if k is None else k
        training_set_percentage = 0.632 if training_set_percentage is None else training_set_percentage

        num_samples = data_set.data.shape[0]
        num_training_samples = round(num_samples * training_set_percentage)

        for i in range(0, k):
            np.random.shuffle(data_set.data)
            training_set = ds.DataSet(data_set.data[:num_training_samples], data_set.labels)
            test_set = ds.DataSet(data_set.data[num_training_samples:], data_set.labels)

            d_tree = dt.DecisionTree(training_set, decision_algorithm)

            aux_confusion_matrix = self.generate_confusion_matrix(d_tree, test_set)

            if self.confusion_matrix is None:
                self.confusion_matrix = aux_confusion_matrix
            else:
                self.confusion_matrix += aux_confusion_matrix

        self.confusion_matrix = np.round(self.confusion_matrix / k, 2)

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

        max_len = len(str(max(max(i) for i in self.confusion_matrix)))
        labels = list(ds.DataSet.labels_possible_values_list[0][1])
        num_total = self.confusion_matrix.sum()

        print('\n\n    Real / Prediction\n')
        print('     ' + "  ".join([str(l).rjust(max_len) for l in ds.DataSet.labels_possible_values_list[0][1]]))
        for value, label in zip(self.confusion_matrix, labels):
            print(str(label) + '    ' + "  ".join([str(l).rjust(max_len) for l in value]))

        print('\n Total: ' + str(num_total))

        print('\n\n    Real / Prediction\n')
        print('     ' + "  ".join([str(l).rjust(max_len) for l in ds.DataSet.labels_possible_values_list[0][1]]))
        for value, label in zip(self.confusion_matrix, labels):
            print(str(label) + '    ' + "  ".join(
                [(str(round(l / num_total * 100)) + '%').rjust(max_len) for l in value]))

        print('\n Total: ' + str(num_total))

    def print_metrics(self):
        if self.confusion_matrix.shape[0] == 2:  # Binary classification

            true_positive = self.confusion_matrix[0][0]
            true_negative = self.confusion_matrix[1][1]
            false_positive = self.confusion_matrix[1][0]
            false_negative = self.confusion_matrix[0][1]

            num_classified_samples = true_positive + true_negative + false_positive + false_negative

            accuracy = (true_positive + true_negative) / num_classified_samples
            precision = true_positive / (true_positive + false_positive)
            recall = true_positive / (true_positive + false_negative)  # True positive recognition rate
            specificity = true_negative / (true_negative + false_positive)  # True negative recognition rate

            f_measure = 2 * true_positive / (2 * true_positive + false_positive + false_negative)

            print()
            print('TP: ' + str(true_positive))
            print('TN: ' + str(true_negative))
            print('FP: ' + str(false_positive))
            print('FN: ' + str(false_negative))
            print()
            print('Number of samples: ' + str(num_classified_samples))
            print()
            print('accuracy: ' + str(accuracy))
            print('precision: ' + str(precision))
            print('recall: ' + str(recall))
            print('specificity: ' + str(specificity))
            print()
            print('f_measure: ' + str(f_measure))
