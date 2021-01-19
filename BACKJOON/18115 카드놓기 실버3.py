import sys
N = int(input())
L = list(map(int,input().split()))
S = []
E = []
for i in range(1,N+1):
    skill = L[N-i]
    if skill == 1:
        S.append(str(i))    
    elif skill == 2:
        S.insert(-1,str(i))
    elif skill == 3:
        E.append(str(i))
S.reverse()
R = S + E
print(' '.join(R))
