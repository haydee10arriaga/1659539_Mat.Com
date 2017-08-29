contador=0

def minimo(arr):
    Arreglo=arr[0]
    global contador
    for H in arr:
        contador+=1
        if(H<Arreglo):
            Arreglo=H
    return Arreglo

def ordenar(arr):
    aux=arr[:]
    arrsort=[]
    for Arreglo in range(len(aux)):
        H=minimo(aux)
        aux.remove(H)
        arrsort.append(H)
    return arrsort

import random
p=random.sample(range(0,100),99)
print("Arreglo desordenado: \n", p)
psort=ordenar(p)
print("\nNumero de operaciones: ", contador)
print("\nArreglo ordenado:\n", psort)
input("Presione Enter para continuar")