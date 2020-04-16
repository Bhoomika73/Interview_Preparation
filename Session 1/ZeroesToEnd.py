#Link: https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array/0 
t = int(input())
for i in range (t):
    n=int(input())
    a=map(int,input().split())
    c=0
    for i in a:
        if i!=0:
            print(i,end=' ')
            c=c+1
    for i in range(n-c):
        print(0,end=' ')
    print('')