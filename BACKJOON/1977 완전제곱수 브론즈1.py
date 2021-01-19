import sys
import math

M = int(input())
N = int(input())

M = math.ceil(math.sqrt(M))
N = int(math.sqrt(N))

SUM = 0
for i in range(M,N+1):
    SUM += pow(i,2)


if SUM == 0:
    print(-1)
else:
    print(SUM)
    print(pow(M,2))
