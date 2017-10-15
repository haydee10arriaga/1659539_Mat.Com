def primo(n):
	cnt=0
	for i in 2,(n**0.5):
		cnt=cnt+1
		if ((n%i)==0):
			#return("no es primo")
			break
		#return("si es primo")
		return cnt


def primo(n):
	cnt=0
	for i in range(2,round(n**0.5)):
		cnt=cnt+1
		if ((n%i)==0):
			break
	return cnt

for w in range(1,10011,50):
    print(w,primo(w))
    
    
    
