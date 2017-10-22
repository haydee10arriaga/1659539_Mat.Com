# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:24:44 2017

@author: Angies computer
"""

from heapq import heappop, heappush


def flatten(L):
     while len(L) > 0:
         yield L[0]
         L = L[1]
 
class Grafo:
  
     def __init__(self):
         self.V = set() # un conjunto
         self.E = dict() # un mapeo de pesos de aristas
         self.vecinos = dict() # un mapeo
  
     def agrega(self, v):
         self.V.add(v)
         if not v in self.vecinos: # vecindad de v
             self.vecinos[v] = set() # inicialmente no tiene nada
  
     def conecta(self, v, u, peso=1):
         self.agrega(v)
         self.agrega(u)
         self.E[(v, u)] = self.E[(u, v)] = peso # en ambos sentidos
         self.vecinos[v].add(u)
         self.vecinos[u].add(v)
  
     def complemento(self):
         comp= Grafo()
         for v in self.V:
             for w in self.V:
                 if v != w and (v, w) not in self.E:
                     comp.conecta(v, w, 1)
         return comp
     
     def shortest(self, v): # Dijkstra's algorithm
        q = [(0, v, ())] # arreglo "q" de las "Tuplas" de lo que se va a almacenar dondo 0 es la distancia, v el nodo y () el "camino" hacia el
        dist = dict() #diccionario de distancias 
        visited = set() #Conjunto de visitados
        while len(q) > 0: #mientras exista un nodo pendiente
            (l, u, p) = heappop(q) # Se toma la tupla con la distancia menor
            if u not in visited: # si no lo hemos visitado
                visited.add(u) #se agrega a visitados
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])  	#agrega al diccionario
            p = (u, p) #Tupla del nodo y el camino
            for n in self.vecinos[u]: #Para cada hijo del nodo actual
                if n not in visited: #si no lo hemos visitado
                    el = self.E[(u,n)] #se toma la distancia del nodo acutal hacia el nodo hijo
                    heappush(q, (l + el, n, p)) #Se agrega al arreglo "q" la distancia actual mas la ditanacia hacia el nodo hijo, el nodo hijo n hacia donde se va, y el camino
        return dist #regresa el diccionario de distancias
     #Algoritmo Dijkstra
     def shortest1(self,v):
        q= [(0, v, ())]
        dist = dict()
        visited = set()
        while len(q) > 0:
            (l, u, p) = heappop(q)
            if u not in visited:
                visited.add(u)
                dist[u]= (1,u,list(flatten(p))[::-1]+[u])
            p= (u,p)
            for n in self.vecinos[u]:
                if n not in visited:
                    el = self.E[(u,n)]
                    heappush(q, (l+el, n, p))
        return dist
   
# Primero 5 nodos con 10 aristas 
print("Primer grafo 5 nodos con 10 aristas")
g=Grafo()
g.conecta('a','b', 2)
g.conecta('a','c', 5)
g.conecta('a','d', 13)
g.conecta('a','e', 6)
g.conecta('b','c', 23)
g.conecta('b','d', 9)
g.conecta('b','e', 6)
g.conecta('c','d', 4)
g.conecta('d','e', 1)
g.conecta('e','c', 8)
print(g.vecinos['a'])
print(g.shortest('a'))

#segundo 10 nodos con 20 aristas
print("Segundo grafo 10 nodos con 20 aristas")
g1=Grafo()
g1.conecta('a','b', 13)
g1.conecta('a','c',5)
g1.conecta('a','d',25)
g1.conecta('a','e',23)
g1.conecta('a','f',9)
g1.conecta('a','h',18)
g1.conecta('a','i',14)
g1.conecta('a','j',2)
g1.conecta('b','c',11)
g1.conecta('b','d',29)
g1.conecta('c','d',15)
g1.conecta('c','e',7)
g1.conecta('d','e',8)
g1.conecta('e','f',16)
g1.conecta('f','g',24)
g1.conecta('g','h',1)
g1.conecta('h','e',17)
g1.conecta('i','j',12)
g1.conecta('j','h',22)
g1.conecta('j','g',30)

print(g1.vecinos['a'])
print(g1.shortest('a'))

#tercero 15 nodos con 30 aristas
print("Tercero grafo 15 nodos con 30 aristas")
g3=Grafo()
g3.conecta('a','b',2)
g3.conecta('a','c',9)
g3.conecta('a','d',4)
g3.conecta('a','e',3)
g3.conecta('a','f',7)
g3.conecta('a','j',1)
g3.conecta('a','h',11)
g3.conecta('a','i',15)
g3.conecta('a','j',18)
g3.conecta('a','k',19)
g3.conecta('a','l',6)
g3.conecta('a','m',8)
g3.conecta('a','n',9)
g3.conecta('a','o',5)
g3.conecta('a','p',16)
g3.conecta('b','c',1)
g3.conecta('b','d',12)
g3.conecta('b','e',14)
g3.conecta('b','f',21)
g3.conecta('b','g',11)
g3.conecta('b','h',4)
g3.conecta('b','j',15)
g3.conecta('b','k',10)
g3.conecta('b','l',3)
g3.conecta('b','m',20)
g3.conecta('b','n',10)
g3.conecta('b','o',7)
g3.conecta('b','p',5)
g3.conecta('c','d',6)
g3.conecta('c','e',13)
print(g3.vecinos['a'])
print(g3.shortest('a'))

#Cuarto 20 nodos con 40 aristas
print("Cuarto grafo 20 nodos con 40 aristas")
g4=Grafo()
g4.conecta('a','b',1)
g4.conecta('a','c',5)
g4.conecta('a','d',23)
g4.conecta('a','e',25)
g4.conecta('a','f',6)
g4.conecta('a','g',8)
g4.conecta('a','h',10)
g4.conecta('a','i',11)
g4.conecta('a','j',12)
g4.conecta('a','k',5)
g4.conecta('b','c',6)
g4.conecta('b','d',27)
g4.conecta('b','e',3)
g4.conecta('b','f',4)
g4.conecta('b','g',14)
g4.conecta('b','h',16)
g4.conecta('b','i',17)
g4.conecta('b','j',7)
g4.conecta('b','k',9)
g4.conecta('b','l',14)
g4.conecta('c','d',19)
g4.conecta('c','e',22)
g4.conecta('c','f',24)
g4.conecta('c','g',28)
g4.conecta('c','h',2)
g4.conecta('c','i',1)
g4.conecta('c','j',10)
g4.conecta('c','k',13)
g4.conecta('c','l',33)
g4.conecta('c','m',37)
g4.conecta('c','n',40)
g4.conecta('c','o',26)
g4.conecta('c','p',29)
g4.conecta('c','q',12)
g4.conecta('c','r',38)
g4.conecta('c','s',13)
g4.conecta('c','t',35)
g4.conecta('d','l',34)
g4.conecta('d','m',21)
g4.conecta('d','n',28)
print(g4.vecinos['a'])
print(g4.shortest('a'))

#Quinto 25 nodos con 50 aristas
print("Quinto grafo 25 nodos con 50 aristas")
g5=Grafo()
g5.conecta('a','b',10)
g5.conecta('a','c',1)
g5.conecta('a','d',9)
g5.conecta('a','e',2)
g5.conecta('a','f',8)
g5.conecta('a','g',3)
g5.conecta('a','h',7)
g5.conecta('a','i',4)
g5.conecta('a','j',6)
g5.conecta('a','k',5)
g5.conecta('a','l',20)
g5.conecta('a','m',11)
g5.conecta('a','n',19)
g5.conecta('a','o',12)
g5.conecta('a','p',18)
g5.conecta('a','q',30)
g5.conecta('a','r',21)
g5.conecta('a','s',29)
g5.conecta('a','t',22)
g5.conecta('a','u',28)
g5.conecta('a','v',13)
g5.conecta('a','w',17)
g5.conecta('a','x',15)
g5.conecta('a','y',16)
g5.conecta('a','z',36)
g5.conecta('b','c',25)
g5.conecta('b','d',26)
g5.conecta('b','e',36)
g5.conecta('b','f',34)
g5.conecta('b','g',32)
g5.conecta('b','h',31)
g5.conecta('b','i',41)
g5.conecta('b','j',47)
g5.conecta('b','k',44)
g5.conecta('b','l',15)
g5.conecta('b','m',12)
g5.conecta('b','n',10)
g5.conecta('b','o',43)
g5.conecta('b','p',46)
g5.conecta('b','q',33)
g5.conecta('b','r',30)
g5.conecta('b','s',24)
g5.conecta('b','t',29)
g5.conecta('c','d',27)
g5.conecta('c','e',13)
g5.conecta('c','f',11)
g5.conecta('c','g',1)
g5.conecta('c','h',6)
g5.conecta('c','i',7)
g5.conecta('c','j',6)
print(g5.vecinos['a'])
print(g5.shortest('a'))