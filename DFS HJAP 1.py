#Haydee Judith Arriaga
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

def DFS(graph,ini):
    visitados=[]
    F=Pila()
    F.meter(ini)
    while (F.longitud>0):
        act=F.obtener()
        if act in visitados:
            continue
        visitados.append(act)
        Vecinos=graph.Vecinos[act]
        for nodo in Vecinos:
            if nodo not in visitados:
                F.meter(nodo)
    return visitados
graph=Grafo()
graph.Conecta(1,2)
graph.Conecta(2,3)
graph.Conecta(3,4)
graph.Conecta(4,5)
graph.Conecta(1,6)
graph.Conecta(6,7)
graph.Conecta(7,8)
graph.Conecta(8,9)
print(DFS(graph,1))
#[1, 6, 7, 8, 9, 2, 3, 4, 5]