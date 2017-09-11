Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def orden_por_insercion(array):	
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

>>> A=[1,6,3,8,10]
>>> A
[1, 3, 6, 8, 10]
>>> 
