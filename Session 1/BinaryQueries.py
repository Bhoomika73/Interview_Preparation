#Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/range-query-2/
a = input()
A = a.split()
q = int(A[1])
B = map(int,input().split())
B = list(B)
Z = {1:"ODD", 0:"EVEN"}
for i in range(1,q+1):
    d = input()
    D = d.split()
    h = int(D[-1])-1
    if D[0] == '1':
        B[h] = 1-B[h]
    if D[0] == '0':
        print(Z.get(B[h])) 