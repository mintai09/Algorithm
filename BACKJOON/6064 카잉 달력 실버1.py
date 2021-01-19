import sys
import math
k = int(input())

def sol(M,N,x,y):
    
    if x == M:
        x = 0
    if y == N:
        y = 0
        
    for i in range(y,(M*N//math.gcd(M,N))+1,N):
        if i % M == x:
            return i
    else:
        return -1
        
for i in range(0,k):
    M,N,x,y = map(int,input().split())
    print(sol(M,N,x,y))
    
