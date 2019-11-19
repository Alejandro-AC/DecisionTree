import numpy as np


class DecisionAlgorithm:

    def __init__(self, algorithm, data_set):
        self.algorithm = algorithm
        self.data_set = data_set

    def decide_class(self, algorithm=None, data_set=None):
        algorithm = self.algorithm if algorithm is None else algorithm
        data_set = self.data_set if data_set is None else data_set

        if algorithm is 'ID3':
            return self.decide_id3(data_set)
        elif algorithm is 'C4.5':
            return self.decide_c45(data_set)
        elif algorithm is 'Gini':
            return self.decide_gini(data_set)
        else:
            print(" INVALID algorithm for decision")
            return -1

    def decide_id3(self, data_set):
        base_entropy = self.calculate_entropy(data_set[:, 0])

        attribute_gain_list = self.calculate_gain(base_entropy, data_set)
        max_gain_attribute_idx = np.argmax(attribute_gain_list[1:]) + 1  # Exclude first since it's the class

        return max_gain_attribute_idx

    def decide_c45(self, data_set):
        base_entropy = self.calculate_entropy(data_set[:, 0])
        attribute_gain_list = self.calculate_gain(base_entropy, data_set)
        attribute_split_info_list = self.calculate_split_info(base_entropy, data_set)

        attribute_gain_ratio_list = self.calculate_gain_ratio(attribute_gain_list, attribute_split_info_list)
        max_gain_ratio_attribute_idx = np.argmax(
            attribute_gain_ratio_list[1:]) + 1  # Exclude first since it's the class

        return max_gain_ratio_attribute_idx

    def decide_gini(self, data_set):
        #base_entropy = self.calculate_entropy(data_set[:, 0])
        #attribute_gini_list = self.calculate_gini(base_entropy, data_set)
        base_gini = self.calculate_gini(data_set[:, 0])

        attribute_gini_gain_list = self.calculate_gini_gain(base_gini, data_set)
        max_gini_gain_attribute_idx = np.argmax(
        attribute_gini_gain_list[1:]) + 1  # Exclude first since it's the class

        return max_gini_gain_attribute_idx

    def calculate_entropy(self, class_values=None, base=None):
        class_values = self.data_set[:, 0] if class_values is None else class_values
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
                value_rows = reduced_matrix[np.where(reduced_matrix[:, 1] == value)]  # Matrix of rows with current val
                gain_list[col] -= count / total_count * self.calculate_entropy(value_rows[:, 0], 2)
                

        return gain_list

    def calculate_split_info(self, base_entropy, data_set):
        
        split_info_list = [0] * data_set.shape[1]
        num_columns = data_set.shape[1]
        for col in range(1,num_columns):
            unique_values, counts = np.unique(data_set[:, col], return_counts=True)
            total_count = counts.sum()
            for value, count in zip(unique_values, counts):
                split_info_list[col]-=(count/total_count)*np.log(count/total_count) / np.log(2)

        return split_info_list

    def calculate_gain_ratio(self, gain_list, split_info_list):
        gain_ratio=[0]*len(gain_list)
        for col in range(1,len(gain_list)):
            if split_info_list[col]!=0:
                gain_ratio[col]=gain_list[col]/split_info_list[col]  

        return gain_ratio

    def calculate_gini(self,  class_values=None, base=None):
         class_values = self.data_set[:, 0] if class_values is None else class_values
         value, counts = np.unique(class_values, return_counts=True)
         norm_counts = counts / counts.sum()
                  

         return 1 - (norm_counts**2).sum()

    def calculate_gini_gain(self, base_entropy=None, data_set=None):
        data_set = self.data_set if data_set is None else data_set

        num_columns = data_set.shape[1]
        gain_list = [base_entropy] * num_columns  # Initialize with base value
        for col in range(1, num_columns):
            unique_values, counts = np.unique(data_set[:, col], return_counts=True)
            total_count = counts.sum()
            reduced_matrix = data_set[:, [0, col]]  # Matrix with only class and current columns
            for value, count in zip(unique_values, counts):
                value_rows = reduced_matrix[np.where(reduced_matrix[:, 1] == value)]  # Matrix of rows with current val
                gain_list[col] -= count / total_count * self.calculate_gini(value_rows[:, 0], 2)

        return []
