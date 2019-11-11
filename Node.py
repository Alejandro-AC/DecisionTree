import DecisionAlgorithm as da
import DataSet as ds
import numpy as np


class Node:

    def __init__(self, data_set, attribute_label=None, attribute_value=None):
        self.children_list = []
        self.data_set = data_set
        self.attribute_label = attribute_label
        self.attribute_value = attribute_value
        self.num_samples = self.data_set.data.shape[0]
        self.class_values, self.class_counts = np.unique(self.data_set.data[:, 0], return_counts=True)

        self.decision_algorithm = da.DecisionAlgorithm('ID3',
                                                       self.data_set.data)  # TODO make it class/global variable of the Tree

        # Check that there is more than 1 column (+ Class) and that Class has different values
        if self.data_set.data.shape[1] > 2 and len(np.unique(self.data_set.data[:, 0])) > 1:
            self.create_children()

    def create_children(self):
        class_label_idx = self.decision_algorithm.decide_class(data_set=self.data_set.data)
        class_label = self.data_set.labels[class_label_idx]
        self.attribute_label = class_label

        for class_value in ds.DataSet.labels_possible_values[class_label]:
            child_subset = self.data_set.create_subset(class_label, class_value)
            child = Node(child_subset, None, class_value)
            self.children_list.append(child)

    def traverse(self, graph, depth=0):
        self.print(depth)

        if depth is 0:
            self.add_root_to_graph(graph)

        for child in self.children_list:
            self.add_child_to_graph(child, graph)

            child.traverse(graph, depth + 1)

    def add_child_to_graph(self, child, graph):
        if not child.class_values.size:
            label = "Samples=" + str(child.num_samples)
        elif len(child.class_values) == 1:
            label = "Value=" + str(child.class_values[0]) + \
                    "\nSamples=" + str(child.num_samples)
        else:
            label = str(child.attribute_label) + \
                    "\nSamples=" + str(child.num_samples) + \
                    "\nClass Counts=" + str(child.class_counts) + \
                    "\nClass Values=" + str(child.class_values)
        graph.node(str(id(child)), label=label)
        graph.edge(str(id(self)), str(id(child)), label=str(child.attribute_value))

    def add_root_to_graph(self, graph):
        graph.node(str(id(self)), label=str(self.attribute_label) +
                                        "\nSamples=" + str(self.num_samples) +
                                        "\nClass Counts=" + str(self.class_counts) +
                                        "\nClass Values=" + str(self.class_values)
                   )

    def print(self, depth):
        print('\n')
        print("".rjust(depth * 3, '-') + " Node Attribute used to decide: " + str(self.attribute_label))
        print("".rjust(depth * 3, ' ') + " Node Number of Samples: " + str(self.num_samples))
        print("".rjust(depth * 3, ' ') + " Node Class Values: " + str(self.class_values))
        print("".rjust(depth * 3, ' ') + " Node Class Counts: " + str(self.class_counts))
        print("".rjust(depth * 3, '-') + " Node Depth: " + str(depth))
        print(self.data_set.data)
