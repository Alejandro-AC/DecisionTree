import pprint
import tree as tr
import nodo as nd


class DecisionTree():

    def __init__(self, directorio):
        self.directorio = directorio
        self.listaDatos = []  ##todos los datos leidos del programa
        self.listaKeys = []  ##lista con todos los posibles valores categoricos de los campos
        self.arrel = None

        self._init_lecturaDatos()
        self._init_crearListaKeys()
        self._init_crearArbol()

    def _init_lecturaDatos(self):

        with open(self.directorio, 'r') as reader:
            for line in reader:
                listaux = []
                for elemento in line.replace("\n", "").split(","):
                    listaux.append(elemento)
                self.listaDatos.append(listaux)

    def _init_crearListaKeys(self):

        for elemento in self.listaDatos:
            i = 0
            for i in range(1, 23):
                self.procesarKeys(elemento[i], i)

    def procesarKeys(self, atribut, pos):
        if len(self.listaKeys) < pos:
            self.listaKeys.append([atribut])
        else:
            if atribut not in self.listaKeys[pos - 1]:
                self.listaKeys[pos - 1].append(atribut)

    def _init_crearArbol(self):
        self.arrel = nd.Nodo(self.listaDatos, self.listaKeys)

    def recorrerArbol(self):
        print("funcion recorrer arbol")
        self.arrel.recorreNodes()

#
#    def printarCAmpos(self): #para debugar
#        print("funcion printar campos")
#        for elemento in self.arrel.dicHijos:
#            print elemento

#    
#    def printarArbol(self):
#
