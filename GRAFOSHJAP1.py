# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:28:54 2017

@author: Angies computer
"""

class Grafo(object):
    def __init__(self):
        self.Vertices=set()
        self.Aristas=dict()
        self.Vecinos=dict()
        
    def Agrega(self,V):
        self.Vertices.add(V)
        if not V in self.Vecinos:
            self.Vecinos[V]=set()
            
    def Conecta(self,U,V,peso=1):
        self.Agrega(U)
        self.Agrega(V)
        self.Aristas[(U,V)]=self.aristas[(V,U)]=peso
        self.Vecinos[U].add(V)
        self.Vecinos[V].add(U)
        
    @property
    def Complemento(self):
        comp=Grafo()
        for A in self.Vertices:
            for B in self.Vertices:
                if A!=B and (A,B) not in self.Aristas:
                    comp.Conecta(A,B,1)
g=Grafo()
g.Conecta('a','b')
g.Conecta('a','c')
g.Conecta('d','e')
g.Conecta('a','e')