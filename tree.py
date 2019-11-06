# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:07:11 2019

@author: Ronny
"""


import copy as c


class Tree():

    def __init__(self, data):
        self.lista = []
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
            
#            if elemento[1]=='b':
#                if elemento[0]=='p':
#                    self.listaEntropia[0][0]=self.listaEntropia[0][0]+1
#                else:
#                    self.listaEntropia[1]=self.listaEntropia[1]+1
#            if elemento[1]=='c':

          #esta funcion crea la lista de diccionarios para las setas que son venenosas, las guarda en self.listaDicVen
    def procesarSumaVen(self,atribut,pos):
        #print(len(self.listaDicVen))
        if len(self.listaDicVen)<pos:
            #print("falta")
            self.listaDicVen.append({atribut:0})
#            print("metido")
#            print(self.listaDicVen)
        else:
           # print("segunda ronda")
            #if pos==1:
                #print(self.listaDicVen)
            if self.listaDicVen[pos-1].has_key(atribut):
                    #print("atributo esta en pos y:")
                    #print(pos-1)                     
                    #print(atribut)
                    #print(self.listaDicVen[pos-1][atribut])
                    self.listaDicVen[pos-1][atribut]=self.listaDicVen[pos-1][atribut]+1
            else:
                self.listaDicVen[pos-1][atribut]=0

                

            
#        
#        
#        print("atribut:")
#        print(atribut)
#        print("pos")
#        print(pos)
#        

            #esta funcion hace lo mismo pero con las que son comestibles, las guarda en self.listaDicEd
    def procesarSumaEd(self,atribut,pos):
        if len(self.listaDicEd)<pos:
            self.listaDicEd.append({atribut:0})
        else:
            if self.listaDicEd[pos-1].has_key(atribut):
                    self.listaDicEd[pos-1][atribut]=self.listaDicEd[pos-1][atribut]+1
            else:
                self.listaDicEd[pos-1][atribut]=0

                
            
            
            
