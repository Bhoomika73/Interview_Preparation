#Link: https://www.codechef.com/problems/LAPIN
t = int(input())
for i in range(0,t):
    S = input()
    L = list(S)
    n = len(L)
    d = n//2
    F = L[:d]
    E = L[-d:]
    F.sort()
    E.sort()
    if F==E:
        print("YES")
    else:
        print("NO")