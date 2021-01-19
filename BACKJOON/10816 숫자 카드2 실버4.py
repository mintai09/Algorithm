import sys
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))


A.sort()

cards = [[] for _ in range(2)]
cards[0] = list(set(A))
cards[0].sort()

cards[1] = [ 0 for _ in range(len(cards[0]))]



j = 0

for i in range(N):
    if cards[0][j] != A[i]:
        j += 1
    cards[1][j] += 1
       
res = [ '0' for _ in range(M)]


for i in range(M):
    s,e = 0,len(cards[0]) - 1
    
    while s <= e:
        m = (s+e) // 2   
        if cards[0][m] == B[i]:
            res[i] = str(cards[1][m])
            break
        elif cards[0][m] > B[i]:
            e = m -1
        else :
            s = m + 1
            
print(' '.join(res))
