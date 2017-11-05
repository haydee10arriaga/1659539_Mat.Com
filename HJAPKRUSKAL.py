from heapq import heappop, heappush
from copy import deepcopy
import random

import time
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst] 
    l = [] # empty list that will store current permutation
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l

class Fila:
    def __init__(self):
        self.fila= []
    def obtener(self):
        return self.fila.pop()
    def meter(self,e):
        self.fila.insert(0,e)
        return len(self.fila)
    @property
    def longitud(self):
        return len(self.fila)

class Pila:
    def __init__(self):
        self.pila= []
    def obtener(self):
        return self.pila.pop()
    def meter(self,e):
        self.pila.append(e)
        return len(self.pila)
    @property
    def longitud(self):
        return len(self.pila)

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

    def BFS(self,ni):
        visitados =[]
        f=Fila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
    
    def DFS(self,ni):
        visitados =[]
        f=Pila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
    
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

    def kruskal(self):
        e = deepcopy(self.E)
        arbol = Grafo()
        peso = 0
        comp = dict()
        t = sorted(e.keys(), key = lambda k: e[k], reverse=True)
        nuevo = set()
        while len(t) > 0 and len(nuevo) < len(self.V):
            #print(len(t)) 
            arista = t.pop()
            w = e[arista]    
            del e[arista]
            (u,v) = arista
            c = comp.get(v, {v})
            if u not in c:
                #print('u ',u, 'v ',v ,'c ', c)
                arbol.conecta(u,v,w)
                peso += w
                nuevo = c.union(comp.get(u,{u}))
                for i in nuevo:
                    comp[i]= nuevo
        print('MST con peso', peso, ':', nuevo, '\n', arbol.E)
        return arbol

    def vecinoMasCercano(self):
        lv = list(self.V)
        random.shuffle(lv)
        ni = lv.pop()
        le = dict()
        while len(lv)>0:
            ln = self.v[ni]
            for nv in ln:
                le[nv]=self.E[(ni,nv)]
            menor = min(le.values())
            lv.append(menor)
            del lv[menor]
        return lv
        			
g= Grafo()#Necesitamos un grafo que este conectado con todos para que pueda encontrar el camino 
g.conecta('a','b', 10)
g.conecta('a','c', 4)
g.conecta('a','d', 17)
g.conecta('a','e', 2)
g.conecta('b','c', 8)
g.conecta('b','d', 6)
g.conecta('b','e', 1)
g.conecta('c','d', 12)
g.conecta('c','e', 9)
g.conecta('d','e', 23)

print(g.kruskal())
print(g.shortest('a'))

print(g)
k = g.kruskal()
#print([print(x, k.E[x]) for x in k.E])

for r in range(50):
    ni = random.choice(list(k.V))
    dfs =  k.DFS(ni)
    c = 0
    #print(dfs)
    #print(len(dfs))
    for f in range(len(dfs) -1):
            c += g.E[(dfs[f],dfs[f+1])]
            print(dfs[f], dfs[f+1],g.E[(dfs[f],dfs[f+1])] )
            
    c += g.E[(dfs[-1],dfs[0])]
    print(dfs[-1], dfs[0], g.E[(dfs[-1],dfs[0])])
    print('costo',c)



m= Grafo()
m.conecta('Guadalupe', 'Apodaca',16)
m.conecta('Guadalupe', 'Juarez',24)
m.conecta('Guadalupe', 'Monterrey',6)
m.conecta('Guadalupe', 'Garcia',43)
m.conecta('Guadalupe', 'San Nicolas',11)
m.conecta('Guadalupe', 'Allende',60)
m.conecta('Guadalupe', 'Escobedo',19)
m.conecta('Guadalupe', 'Linares',131)
m.conecta('Guadalupe', 'Pesqueria',29)

m.conecta('Apodaca','Juarez',26)
m.conecta('Apodaca','Monterrey',20)
m.conecta('Apodaca','Garcia',46)
m.conecta('Apodaca','San Nicolas',14)
m.conecta('Apodaca','Allende',75)
m.conecta('Apodaca','Escobedo',23)
m.conecta('Apodaca','Linares',147)
m.conecta('Apodaca','Pesqueria',16)

m.conecta('Juarez','Monterrey',31)
m.conecta('Juarez','Garcia',74)
m.conecta('Juarez','San Nicolas',36)
m.conecta('Juarez','Allende',50)
m.conecta('Juarez','Escobedo',44)
m.conecta('Juarez','Linares',90)
m.conecta('Juarez','Pesqueria',32)

m.conecta('Monterrey','Garcia',37)
m.conecta('Monterrey','San Nicolas',9)
m.conecta('Monterrey','Allende',59)
m.conecta('Monterrey','Escobedo',15)
m.conecta('Monterrey','Linares',130)
m.conecta('Monterrey','Pesqueria',36)

m.conecta('Garcia','San Nicolas',51)
m.conecta('Garcia','Allende',93)
m.conecta('Garcia','Escobedo',34)
m.conecta('Garcia','Linares',165)
m.conecta('Garcia','Pesqueria',65)

m.conecta('San Nicolas','Allende',66)
m.conecta('San Nicolas','Escobedo',8)
m.conecta('San Nicolas','Linares',136)
m.conecta('San Nicolas','Pesqueria',38)

m.conecta('Allende','Escobedo',76)
m.conecta('Allende','Linares',72)
m.conecta('Allende','Pesqueria',76)

m.conecta('Escobedo','Linares',148)
m.conecta('Escobedo','Pesqueria',36)

m.conecta('Linares','Pesqueria',148)




k = m.kruskal()
for r in range(50):
    ni = random.choice(list(k.V))
    dfs =  k.DFS(ni)
    c = 0
    #print(dfs)
    #print(len(dfs))
    for f in range(len(dfs) -1):
            c += m.E[(dfs[f],dfs[f+1])]
            print(dfs[f], dfs[f+1], m.E[(dfs[f],dfs[f+1])] )
            
    c += m.E[(dfs[-1],dfs[0])]
    print(dfs[-1], dfs[0], m.E[(dfs[-1],dfs[0])])
    print('costo',c,'\n')



import time
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst] 
    l = [] # empty list that will store current permutation
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l


data = list('abcdefghij')
tim=time.clock()
per = permutation(data)
print(time.clock()-tim)