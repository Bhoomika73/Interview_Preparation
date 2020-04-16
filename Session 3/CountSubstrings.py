#Link: https://www.codechef.com/problems/CSUB
t = int(input())
for i in range(0,t):
    n = int(input())
    S = input()
    L = list(S)
    c = L.count("1")
    p=(c*(c-1))//2
    print(p+c)