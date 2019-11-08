# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:07:11 2019

@author: Ronny
"""


import copy as c
import math as m


class Tree():

    def __init__(self, data):
        self.lista = [] ##lista de los datos
        self.listaEntropia=[]
        self.lista1=[]
        self.listaProc=[]
        self.listaDicVen=[] ##lista para los 
        self.listaDicEd=[]
        
        self._init_lista(data)
        self._init_clasificaEntropia()

    def _init_lista(self, data):
        with open(data, 'r') as reader:
           
            for line in reader:
                listaux=[] 
                for elemento in line.replace("\n","").split(","):
                    listaux.append(elemento)
                    
                self.lista.append(listaux)
    
            
    def printLista(self):
        print(self.listaDicVen)
        
    
    def _init_clasificaEntropia(self):
        
        for elemento in self.lista:
            i=0
            for i in range(1,23):
                if elemento[0]=='p':
                    self.procesarSumaVen(elemento[i],i)
                else:
                    self.procesarSumaEd(elemento[i],i)
        print(self.listaDicVen)
        print(self.listaDicEd)

          #esta funcion crea la lista de diccionarios para las setas que son venenosas, las guarda en self.listaDicVen
    def procesarSumaVen(self,atribut,pos):
        if len(self.listaDicVen)<pos:
            self.listaDicVen.append({atribut:0})
        else:

            if self.listaDicVen[pos-1].has_key(atribut):

                    self.listaDicVen[pos-1][atribut]=self.listaDicVen[pos-1][atribut]+1
            else:
                self.listaDicVen[pos-1][atribut]=0

            #esta funcion hace lo mismo pero con las que son comestibles, las guarda en self.listaDicEd
    def procesarSumaEd(self,atribut,pos):
        if len(self.listaDicEd)<pos:
            self.listaDicEd.append({atribut:0})
        else:
            if self.listaDicEd[pos-1].has_key(atribut):
                    self.listaDicEd[pos-1][atribut]=self.listaDicEd[pos-1][atribut]+1
            else:
                self.listaDicEd[pos-1][atribut]=0

                
    def guany(self):
        listaC = []    # caracterisiticas que hay comestibles y venenosos 
        listaSE = []   # solo comestibles
        listaSV = []   #solo venenosos
        Total = 0
        H = 0
        H_menor = 10000
        Atributo = 0

        for key in self.listaDicVen[0]:
            Total = Total + self.listaDicVen[0][key]
        for key in self.listaDicEd[0]:
            Total = Total + self.listaDicEd[0][key]
            
            
        for i in range(len(self.listaDicVen)): 
            listaC = []
            for key in self.listaDicVen[i]:
                if (self.listaDicEd[i].has_key(key)):  
                    #print(key)
                    listaC.append(key)
                '''else:
                    listaSV.append(key)'''
                    
            '''for key in self.listaDicEd[i]:
                if (key not in listaC):
                    listaSE.append(key)'''
            ###los casos en que sea +0 -n  o  +n -0   H = 0 y por tanto
            ### no hace falta hacerlos, solo en caso que len(listaC) == 0 
            ### tener en cuenta que toda la H sera 0
            
            if(len(listaC) != 0):    
                for j in listaC:
                    veneno = float(self.listaDicVen[i][j])
                    comestible = float(self.listaDicEd[i][j])
                    H = 0
                    
                    St = veneno + comestible
                    
                    H = H - (veneno/St) * m.log((veneno/St), 2)
                    H = H - (comestible/St) * m.log((comestible/St), 2)
                    H = (St/Total)*H
            else:
                H = 0
           
            print (H)
            print(St)
            print(Total)
            if (H < H_menor):
                H_menor = H
                Atributo = i + 1
                
        print(Atributo)
        return Atributo
                        
        
        
        
        """     for j in range(len(lista2)):
            for i in range(len(lista2[j])):
                St = lista2[j][i+1] + lista2[j][i]
                H = H + (lista2[j][i]/St) * m.log((lista2[j][i]/St), 2)
                H = H + (lista2[j][i+1]/St) * m.log((lista2[j][i+1]/St), 2)
                H = (St/Total)*H
        
        if(H <= mejorH):
            mejorH = H
            Atributo = j """       
            
            
