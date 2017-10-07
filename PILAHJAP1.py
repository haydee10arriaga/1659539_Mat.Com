# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:44:40 2017

@author: Angies computer
"""
class Pila(object):
    def __init__(self):
        self.pila=[]
    def obtener(self):
        return self.pila.pop()
    def meter(self,e):
        self.pila.append(e)
        return len(self.pila)
    @property
    def longitud(self):
        return len(self.pila)
        
p=Pila()
p.meter(5)
p.meter("pila")
p.meter("hello")
print(p.longitud)
print(p.obtener())
print(p.obtener())
print(p.obtener())
print(p.longitud)
            
            
