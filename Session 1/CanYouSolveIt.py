#Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/can-you-solve-it/
t = int(input())
for i in range(t):
    n = int(input())
    L = list(map(int,input().split()))
    M = []
    N = []
    for i in range(n):
        N.append(L[i]+i)
        M.append(L[i]-i)
    m = max(M)-min(M)
    n = max(N)-min(N)
    print(max(m,n))