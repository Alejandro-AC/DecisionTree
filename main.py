# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:56:23 2019

@author: Ronny
"""


import tree as tr
import nodo as nd
import DecisionTree as dt




if __name__ == "__main__":
    dirFichero = 'data/agaricus-lepiota.data'
    arbol=dt.DecisionTree(dirFichero)
    arbol.recorrerArbol()
    
    
    