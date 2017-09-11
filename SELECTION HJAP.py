#Haydee Judith Arriaga Ponce 
#algoritmo de ordenacion selection
cnt=0
def selection(arr):
	global cnt
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
	return arr

>>> A=[9,6,4,2,3]
>>> A
[9, 6, 4, 2, 3]
>>> selection(A)
[2, 3, 4, 6, 9]
>>>