#Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/long-atm-queue-3/
a = int(input())
B = list(map(int,input().split()))
c=1
for i in range(0,a-1):
    if (B[i] > B[i+1]):
        c = c+1
print(c)