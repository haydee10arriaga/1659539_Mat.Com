def fiboiter(n):
    global cnt
    fib=[1,1]
    for k in range(2,n+1):
        fib.append(fib[k-1]+fib[k-2])
    return fib[n]

for n in range(0,31):
    print(n,fiboiter(n))
