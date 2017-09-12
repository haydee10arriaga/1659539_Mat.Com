#Haydee Judith Arriaga Ponce 
#insercion algoritmo de ordenacion 
cnt=0
def orden_por_insercion(array):	
	global cnt
	for indice in range(1,len(array)):
		valor=array[indice] #valor es el elemento que vamos a comparar
		i=indice-1 #i es el valor anterior al elemento que estamos comparando
		while 1>=0:
			cnt+=1
			if valor<array[i]: #comparamos valor con el elemento anterior 
				array[i+1]=array[i] #intercambiamos los valores 
				array[i]=valor
				i-=1 #decrementamos en 1 el valor de i
			else:
				break
	return array

print("Arreglo DESORDENADO: ")
A=[1,6,3,8,5]
print(A)
print("Arreglo ORDENADO: \n", orden_por_insercion(A))
input("Presione Enter para continuar")