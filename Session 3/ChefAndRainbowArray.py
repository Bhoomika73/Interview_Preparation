#Link: https://www.codechef.com/problems/RAINBOWA
import math
t = int(input())
for i in range(t):
    n = int(input())
    L = list(map(int,input().split()))
    M=[]
    if L!=L[::-1]:
        print("no")
    else:
        for i in L:
            if i not in M:
                M.append(i)
        if (M==[1,2,3,4,5,6,7]):
            print("yes")
        else:
            print("no")