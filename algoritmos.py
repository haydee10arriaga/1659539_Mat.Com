
import random
import copy

def ran_num(n,lim_inf=0, lim_sup=100):
    arreglo = []                  
    for i in range(n):
        arreglo.append(random.randint(lim_inf, lim_sup))
    return arreglo


def burbuja(A):
	cnt=0
	for i in range(1,len(A)):
			for j in range(0, len(A)-1):
				cnt+=1
				if(A[j+1]<A[j]):
					aux=A[j]
					A[j]=A[j+1]
					A[j+1]=aux
	return cnt

def selection(arr):
	cnt=0
	for i in range (0,len(arr)-1):
		val=i
		for j in range(i+1,len(arr)):
			cnt=cnt+1
			if arr[j]<arr[val]:
				val=j
		if val!=i:
			aux=arr[i]
			arr[i]=arr[val]
			arr[val]=aux
	return cnt

def orden_por_insercion(array):	
    cnt=0
    for indice in range(1,len(array)):
        i = indice
        #valor=array[indice] #valor es el elemento que vamos a comparar
        #i=indice-1 #i es el valor anterior al elemento que estamos comparando
        while i>0 and array[i]<array[i-1]:
            cnt+=1
            aux = array[i-1]
            array[i-1]=array[i] #intercambiamos los valores 
            array[i]=aux
            i-=1 #decrementamos en 1 el valor de i
    return cnt


def quicksort(arr):
	global cnt
	if len(arr) < 2:
		return arr
	p = arr.pop(0)
	menores, mayores = [],[]
	for e in arr:
		cnt +=1
		if e <= p:
			menores.append(e)
		else:
			mayores.append(e)
	return quicksort(menores) + [p] + quicksort(mayores) 


longitud = 2
print("Longitud", "Burbuja", "Selection", "Insertion")
while longitud < 2000:
    arreglo = ran_num(longitud)
    arreglo1, arreglo2, arreglo3, arreglo4 = copy.deepcopy(arreglo), copy.deepcopy(arreglo),copy.deepcopy(arreglo),copy.deepcopy(arreglo)    
    b=burbuja(arreglo1)
    s=selection(arreglo2)
    i=orden_por_insercion(arreglo3)
    cnt = 0
    quicksort(arreglo4)
    print(longitud, b,s,i,cnt)
    longitud = longitud + 50
    

