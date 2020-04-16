#Link: https://practice.geeksforgeeks.org/problems/remove-duplicates/0
t = int(input())
for i in range(0,t):
    S = input()
    L = []
    for i in S:
        if i not in L:
            L.append(i)
    print(*L,sep="")   