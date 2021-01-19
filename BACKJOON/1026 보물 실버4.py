import sys

N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
         
A.sort()
B.sort(reverse=True)
C = []

for i in range(N):
    C.append(A[i]*B[i])
    
print(sum(C))
