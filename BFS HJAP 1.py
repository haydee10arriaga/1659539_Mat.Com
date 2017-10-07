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

def BFS(graph,ini):
    visitados=[ini]
    F=Fila()
    F.meter(ini)
    while (F.longitud>0):
        act=F.obtener()
        Vecinos=graph.Vecinos[act]
        for nodo in Vecinos:
            if nodo not in visitados:
                visitados.append(nodo)
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
print(BFS(graph,1))    
#[1, 2, 6, 3, 7, 4, 8, 5, 9]