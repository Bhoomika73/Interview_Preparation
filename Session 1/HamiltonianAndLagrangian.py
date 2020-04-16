#Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/hamiltonian-and-lagrangian/
n=int(input())
A=map(int,input().split())
A = list(A)
m=A[n-1]
L = []
c=0
for i in range(n-1,-1,-1):
    if A[i]>=m:
        m=A[i]
        L.append(m)
        c=c+1
L.reverse()
print(*L,sep = " ")