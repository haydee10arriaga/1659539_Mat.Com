# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:53:15 2017

@author: Angies computer
"""

#Haydee Judith Arriaga
class Fila(object):
    def __init__(self):
        self.fila=[]
    def obtener(self):
        return self.fila.pop(0)
    def meter(self,e):
        self.fila.append(e)
        return len(self.fila)
    @property
    def longitud(self):
        return len(self.fila)


fila=Fila()
fila.meter(5)
fila.meter('fila')
fila.meter("hello")
print(fila.longitud)
print(fila.obtener())
print(fila.obtener())
print(fila.obtener())
print(fila.longitud)