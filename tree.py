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
        self.listaDicVen=[]
        self.listaDicEd=[]
        
        self._init_lista(data)
        self._init_clasificaEntropia()

    def _init_lista(self, data):
        with open(data, 'r') as reader:
            for y in range(24):
                self.listaEntropia.append(0)
                self.lista1.append(0)
            for j in range(22):
                self.listaEntropia.append(self.lista1)
                
            
            for line in reader:
                listaux=[] 
                for elemento in line.replace("\n","").split(","):
                    listaux.append(elemento)
                    
                self.lista.append(listaux)
    
            
    def printLista(self):
        print(self.lista)
    
    def _init_clasificaEntropia(self):
        
        for elemento in self.lista:
            i=0
            for i in range(1,22):
                if elemento[0]=='p':
                    self.procesarSumaVen(elemento[i],i)
#                else:
                    #self.procesarSumaEd(elemento[i],i)
                
            
#            if elemento[1]=='b':
#                if elemento[0]=='p':
#                    self.listaEntropia[0][0]=self.listaEntropia[0][0]+1
#                else:
#                    self.listaEntropia[1]=self.listaEntropia[1]+1
#            if elemento[1]=='c':

          
    def procesarSumaVen(self,atribut,pos):
#        print(len(self.listaDicVen))
        if len(self.listaDicVen)<pos:
            print("falta")
            self.listaDicVen.append({atribut,0})
            print("metido")
            print(self.listaDicVen)
            
#        
#        
#        print("atribut:")
#        print(atribut)
#        print("pos")
#        print(pos)
#        

            
    def procesarSumaEd(self,atribut,pos):
        print(" ")
  
            
            
            
            
