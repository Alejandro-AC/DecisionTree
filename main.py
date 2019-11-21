# -*- coding: utf-8 -*-

import DataSet as ds
import argparse
import Evaluation as ev
import numpy as np

if __name__ == '__main__':
    dirFichero = 'data/agaricus-lepiota.data'

    ds.DataSet.labels_possible_values = {
        'class': ['e', 'p'],
        'cap-shape': ['b', 'c', 'x', 'f', 'k', 's'],
        'cap-surface': ['f', 'g', 'y', 's'],
        'cap-color': ['n', 'b', 'c', 'g', 'r', 'p', 'u', 'e', 'w', 'y'],
        'bruises?': ['t', 'f'],
        'odor': ['a', 'l', 'c', 'y', 'f', 'm', 'n', 'p', 's'],
        'gill-attachment': ['a', 'd', 'f', 'n'],
        'gill-spacing': ['c', 'w', 'd'],
        'gill-size': ['b', 'n'],
        'gill-color': ['k', 'n', 'b', 'h', 'g', 'r', 'o', 'p', 'u', 'e', 'w', 'y'],
        'stalk-shape': ['e', 't'],
        'stalk-root': ['b', 'c', 'u', 'e', 'z', 'r', '?'],
        'stalk-surface-above-ring': ['f', 'y', 'k', 's'],
        'stalk-surface-below-ring': ['f', 'y', 'k', 's'],
        'stalk-color-above-ring': ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'],
        'stalk-color-below-ring': ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'],
        'veil-type': ['p', 'u'],
        'veil-color': ['n', 'o', 'w', 'y'],
        'ring-number': ['n', 'o', 't'],
        'ring-type': ['c', 'e', 'f', 'l', 'n', 'p', 's', 'z'],
        'spore-print-color': ['k', 'n', 'b', 'h', 'r', 'o', 'u', 'w', 'y'],
        'population': ['a', 'c', 'n', 's', 'v', 'y'],
        'habitat': ['g', 'l', 'm', 'p', 'u', 'w', 'd']
    }

    ds.DataSet.labels_possible_values_list = np.array([
        ['class', ['e', 'p']],
        ['cap-shape', ['b', 'c', 'x', 'f', 'k', 's']],
        ['cap-surface', ['f', 'g', 'y', 's']],
        ['cap-color', ['n', 'b', 'c', 'g', 'r', 'p', 'u', 'e', 'w', 'y']],
        ['bruises?', ['t', 'f']],
        ['odor', ['a', 'l', 'c', 'y', 'f', 'm', 'n', 'p', 's']],
        ['gill-attachment', ['a', 'd', 'f', 'n']],
        ['gill-spacing', ['c', 'w', 'd']],
        ['gill-size', ['b', 'n']],
        ['gill-color', ['k', 'n', 'b', 'h', 'g', 'r', 'o', 'p', 'u', 'e', 'w', 'y']],
        ['stalk-shape', ['e', 't']],
        ['stalk-root', ['b', 'c', 'u', 'e', 'z', 'r', '?']],
        ['stalk-surface-above-ring', ['f', 'y', 'k', 's']],
        ['stalk-surface-below-ring', ['f', 'y', 'k', 's']],
        ['stalk-color-above-ring', ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y']],
        ['stalk-color-below-ring', ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y']],
        ['veil-type', ['p', 'u']],
        ['veil-color', ['n', 'o', 'w', 'y']],
        ['ring-number', ['n', 'o', 't']],
        ['ring-type', ['c', 'e', 'f', 'l', 'n', 'p', 's', 'z']],
        ['spore-print-color', ['k', 'n', 'b', 'h', 'r', 'o', 'u', 'w', 'y']],
        ['population', ['a', 'c', 'n', 's', 'v', 'y']],
        ['habitat', ['g', 'l', 'm', 'p', 'u', 'w', 'd']]
    ])

    ds.DataSet.missing_value_indicator = '?'

    # Decision algorithms: - C45 - ID3 - Gini
    # Evaluation methods: - Holdout - Cross-Validation - Bootstrap

    # Initialize the parser
    parser = argparse.ArgumentParser(
        description="DataSet evaluation with DecisionAlgorithms"
    )

    parser.add_argument('-k', help="number of iterations for Cross-Validation or Bootstrap evaluation methods", type=int)
    parser.add_argument('-trainpercentage', help="Percentage of the dataset destined to the training subset (Between 0 and 1)", type=float)

    parser.add_argument("-a", help="Use Advanced missing values processing", action="store_true")
    parser.add_argument("-l",
                        help="Use Leave one out with Cross-Validation Evaluation method (may take several minutes to complete)")

    parser.add_argument("-c", help="Use C4.5 Decision Algorithm", action="store_true")
    parser.add_argument("-i", help="Use ID3 Decision Algorithm", action="store_true")
    parser.add_argument("-g", help="Use Gini Decision Algorithm", action="store_true")

    parser.add_argument("-o", help="Use Holdout Evaluation method", action="store_true")
    parser.add_argument("-v", help="Use Cross-Validation Evaluation method", action="store_true")
    parser.add_argument("-b", help="Use Bootstrap Evaluation method", action="store_true")

    # Parse the arguments
    arguments = parser.parse_args()

    if arguments:
        advanced_missing_values = None
        leave_one_out = None
        training_set_percentage = arguments.trainpercentage
        k = arguments.k
        evaluation_method = 'Holdout'
        decision_algorithm = 'ID3'

        print("\n")
        if arguments.a:
            print("Using Advanced missing values processing")
            advanced_missing_values = True

        if arguments.l:
            print("Using Leave one Out evaluation")
            leave_one_out = True

        if arguments.c:
            decision_algorithm = 'C45'
        elif arguments.i:
            decision_algorithm = 'ID3'
        elif arguments.g:
            decision_algorithm = 'Gini'

        print('Decision algorithm used: ' + decision_algorithm)

        if arguments.o:
            evaluation_method = 'Holdout'
        elif arguments.v:
            evaluation_method = 'Cross-Validation'
        elif arguments.b:
            evaluation_method = 'Bootstrap'

        print('Evaluation method used: ' + evaluation_method)

        ev.Evaluation(dirFichero, decision_algorithm, evaluation_method, k=k, leave_one_out=leave_one_out,
                      training_set_percentage=training_set_percentage,
                      advanced_missing_values=advanced_missing_values)
