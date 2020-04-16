#Link: https://www.codechef.com/problems/COPS
t = int(input())
for i in range(0,t):
    A = list(map(int,input().split()))
    L = list(map(int,input().split()))
    F = list(range(1,101))
    n = A[1]*A[2]
    for i in L:
        ini = i-n
        if ini<0:
            ini=1
        fin = i+n
        if fin>100:
            fin=100
        for i in range(ini,fin+1):
            if i in F:
                F.remove(i)    
    print(len(F))