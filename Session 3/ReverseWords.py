#Link: https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0
t = int(input())
for i in range(0,t):
    S = input()
    L = S.split('.')
    L = L[::-1]
    print(*L,sep=".")    