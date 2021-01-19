import sys
N,K = map(int,input().split())

def sol(N,K):
    if K == 1:
        return 1
    if K == 2:
        return N+1
    
    s = [  i+1 for i in range(0,N+1)]
    
    while K > 2:
        temp = s[:]
        temp[1] += 1
        for i in range(1,N+1):
            temp[i] = sum(s[0:i+1])
        s = temp[:]
        K -= 1
    return s[N]

print(sol(N,K) % 1000000000)
