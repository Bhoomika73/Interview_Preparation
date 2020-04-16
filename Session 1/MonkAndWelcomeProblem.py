#Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-welcome-problem/
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = []
for i in range(0,n):
    c = A[i]+B[i]
    C.append(c)
for i in range(0,n):
    print(C[i],end = " ")