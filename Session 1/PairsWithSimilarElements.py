#Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/pairs-having-similar-element-eed098aa/
a = int(input())
B = list(map(int,input().split()))
B.sort()
l=len(B)
c=0
D = []
for i in range(0,l-1):
    if B[i+1] == B[i]+1:
        c = c+1 
        if B[i] in D and B[i+1] not in D :
            c=c+1
            D.append(B[i+1])
        elif B[i] and B[i+1] not in D:
            D.append(B[i])
            D.append(B[i+1])   
        if B.count(B[i]) != 1:
            p = B.count(B[i])
            c=c+p
print(c)