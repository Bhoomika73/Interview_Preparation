#Link: https://codezen.codingninjas.com/practice/465/704/stocks-are-profitable
a = int(input())
B = list(map(int,input().split()))
maxi=0
for i in range(0,a):
    for j in range(i+1,a):
        k = B[j] - B[i]
        if k>maxi:
            maxi=k
print(maxi)