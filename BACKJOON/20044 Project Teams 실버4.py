import sys
N = int(input())
L = list(map(int,input().split()))
        
L.sort()
S = 200002
s = 0
e = 2*N - 1

for i in range(0,N):
    if L[i] + L[2*N-1-i] < S:
        S = L[i] + L[2*N-1-i]
print(S)
