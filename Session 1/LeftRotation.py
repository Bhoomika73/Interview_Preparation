#Link: https://www.hackerrank.com/challenges/array-left-rotation/problem
A = list(map(int,input().split()))
B = list(map(int,input().split()))
d=A[1]%A[0]
C = B[:d]
E = B[d:]
print(*E,*C,sep=" ")
