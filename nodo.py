# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:36:32 2019

@author: Ronny
"""
import copy as c

import math as m


class Nodo():

    def __init__(self, data, listaKeys, categoriaNodo="arrel", contadorBucle=0):  ##contadorBucle es para debugar
        self.dicHijos = []
        self.listaDicEd = []
        self.listaDicVen = []
        self.tablaDatos = data
        self.listaKeys = listaKeys
        self.atributoSelec = ""
        self.dataHijos = data
        self.categoriaNodo = categoriaNodo
        self.finalFulla = False
        self.contadorBucle = contadorBucle

        self._init_debugexiste()  ###pruebas
        self._init_clasificaEntropia()
        self.crearHijos()

    def _init_debugexiste(self):  ##funcion solo para debuggin
        listadebug = []
        for elemento in self.dataHijos:
            if (elemento[14] == 'g') and (
                    elemento[8] == 'n'):  # añadir en el if cualquier campo que quieras comprobar si existe o no
                listadebug.append(elemento)
        print("Lista debug:")
        print
        listadebug
        print("------")

    def _init_clasificaEntropia(self):
        print("categoriaNodo: " + str(self.categoriaNodo))
        print("Contador h: " + str(self.contadorBucle))
        for elemento in self.dataHijos:
            i = 0
            for i in range(1, 23):
                if elemento[0] == 'p':
                    self.procesarVen(elemento[i], i)
                else:
<<<<<<< HEAD
                    self.procesarNoVen(elemento[i],i)
        self.atributoSelec= self.guany() +1 
        

    def procesarVen(self,atribut,pos):
        
        if len(self.listaDicVen)<pos:
            self.listaDicVen.append({atribut:0})
        else:    
            if self.listaDicVen[pos-1].has_key(atribut):
                self.listaDicVen[pos-1][atribut]=self.listaDicVen[pos-1][atribut]+1
=======
                    self.procesarNoVen(elemento[i], i)
        self.atributoSelec = self.guany()

    def procesarVen(self, atribut, pos):

        if len(self.listaDicVen) < pos:
            self.listaDicVen.append({atribut: 0})
        else:
            if self.listaDicVen[pos - 1].has_key(atribut):
                self.listaDicVen[pos - 1][atribut] = self.listaDicVen[pos - 1][atribut] + 1
>>>>>>> 92f69c17026b0a1bfbb48d1264890f9993e0b727
            else:
                self.listaDicVen[pos - 1][atribut] = 0

    def procesarNoVen(self, atribut, pos):
        if len(self.listaDicEd) < pos:
            self.listaDicEd.append({atribut: 0})
        else:
            if self.listaDicEd[pos - 1].has_key(atribut):
                self.listaDicEd[pos - 1][atribut] = self.listaDicEd[pos - 1][atribut] + 1
            else:
                self.listaDicEd[pos - 1][atribut] = 0

    def guany(self):  ###LA FUNCION NO VA CORRECTAMENTE  ----REVISAR-----
        listaC = []  # caracterisiticas que hay comestibles y venenosos
        Total = 0
        H = 0
        St = 0
        H_menor = 10000
        Atributo = 0
        print("Data set inical:")  # para ver en pantalla con que datos trabajara guany
        print
        self.listaDicEd
        print("-----")
        print
        self.listaDicVen
        print("-----")

        if len(
                self.listaDicVen) > 0:  ##comprobamos que las opciones que nos quedan con la variable pasada son venenossas
            for key in self.listaDicVen[0]:
                Total = Total + self.listaDicVen[0][key]
        if len(
                self.listaDicEd) > 0:  ##lo mismo para las no venenosass, asi cuando ya no queda ninguna por tratar no se calcula la H
            for key in self.listaDicEd[0]:
                Total = Total + self.listaDicEd[0][key]

            for i in range(len(self.listaDicVen)):
                listaC = []
                for key in self.listaDicVen[i]:
                    if (self.listaDicEd[i].has_key(key)):
                        listaC.append(key)
                ###los casos en que sea +0 -n  o  +n -0   H = 0 y por tanto
                ### no hace falta hacerlos, solo en caso que len(listaC) == 0 
                ### tener en cuenta que toda la H sera 0
<<<<<<< HEAD
                
                if(len(listaC) != 0): 
                    H = 0
                    for j in listaC:
                        veneno = float(self.listaDicVen[i][j])
                        comestible = float(self.listaDicEd[i][j])
                        #H = 0
                        a = 0
                        St = veneno + comestible
                        
                        a = a - (veneno/St) * m.log((veneno/St), 2)
                        a = a - (comestible/St) * m.log((comestible/St), 2)
                        H =  H + (St/Total)*a
=======

                if (len(listaC) != 0):
                    for j in listaC:
                        veneno = float(self.listaDicVen[i][j])
                        comestible = float(self.listaDicEd[i][j])
                        H = 0

                        St = veneno + comestible

                        H = H - (veneno / St) * m.log((veneno / St), 2)
                        H = H - (comestible / St) * m.log((comestible / St), 2)
                        H = (St / Total) * H
>>>>>>> 92f69c17026b0a1bfbb48d1264890f9993e0b727
                else:
                    H = 0
                if (H < H_menor) and (H > 0):
                    H_menor = H
                    Atributo = i
<<<<<<< HEAD
                    #Atributo = Atributo + 1
                #print (H)
                #print(St)
                #print(Total)
            print("La seleccion es:")        
            print(Atributo)
            print H_menor
               
        return Atributo
        
    def crearHijos(self):
        print("FUNCION Creamos hijos------")
        print ("h: num "+ str(self.contadorBucle))
        datosAuxHijosCat=[]        
#        for elemento in self.dataHijos:        "no quitaremos el elemento para facilitar el prog"
#            elemento.pop(self.atributoSelec)
#        if self.finalFulla==False:
        if (len(self.listaDicEd) >0) and (len(self.listaDicVen) >0):
                print("Columnna seleccionada: "+str(self.atributoSelec + 1))

                for campo in self.listaKeys[self.atributoSelec]:
                    for elemento in self.dataHijos:
    #                    print elemento[self.atributoSelec]
                        if elemento[self.atributoSelec] == campo:
    #                        print("es igual")
                            datosAuxHijosCat.append(elemento)
                            
                    if (self.contadorBucle <= 2):  ##para cortar la profunidad en 3 para el debug
                        print("Creamos hijo para el campo: "+str(campo)+ " de la columna "+str(self.atributoSelec))
                        print("Estamos en"+str(self.categoriaNodo)+" la cual tiene " +str(len(self.listaKeys[self.atributoSelec-1]))+" hijos")

                        self.dicHijos.append([self.atributoSelec, Nodo(datosAuxHijosCat,self.listaKeys,campo,self.contadorBucle+1)])    
                        print("Funcion hijos TERMINADA en h: "+str(self.contadorBucle))
                    datosAuxHijosCat=[]
        else:
            print("No creamos mas hijos")
=======
            print("La seleccion es:")
            print(Atributo)
            print(H_menor)

        return Atributo

    def crearHijos(self):
        print("FUNCION Creamos hijos------")
        print("h: num " + str(self.contadorBucle))
        datosAuxHijosCat = []
        #        for elemento in self.dataHijos:        "no quitaremos el elemento para facilitar el prog"
        #            elemento.pop(self.atributoSelec)
        #        if self.finalFulla==False:
        if (len(self.listaDicEd) > 0) and (len(self.listaDicVen) > 0):
            print("Columnna seleccionada: " + str(self.atributoSelec))

            for campo in self.listaKeys[self.atributoSelec - 1]:
                for elemento in self.dataHijos:
                    #                    print elemento[self.atributoSelec]
                    if elemento[self.atributoSelec] == campo:
                        #                        print("es igual")
                        datosAuxHijosCat.append(elemento)
>>>>>>> 92f69c17026b0a1bfbb48d1264890f9993e0b727

                if (self.contadorBucle <= 3):  ##para cortar la profunidad en 3 para el debug
                    print("Creamos hijo para el campo: " + str(campo) + " de la columna " + str(self.atributoSelec))
                    print("Estamos en" + str(self.categoriaNodo) + " la cual tiene " + str(
                        len(self.listaKeys[self.atributoSelec - 1])) + " hijos")

                    self.dicHijos.append(
                        [self.atributoSelec, Nodo(datosAuxHijosCat, self.listaKeys, campo, self.contadorBucle + 1)])
                    print("Funcion hijos TERMINADA en h: " + str(self.contadorBucle))
                datosAuxHijosCat = []
        else:
            print("No creamos mas hijos")

    def recorreNodes(self):
        print("Nodo: " + str(self.categoriaNodo))
        for element in self.dicHijos:
            print("Hijo de " + str(self.categoriaNodo) + ": ")
            element[1].recorreNodes()
