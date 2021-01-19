import sys

N,K = map(int,input().split())
A = list(map(int,input().split()))
result = 0

def dfs(cnt,v,e):
    global result
    
    if cnt == N:
        result += 1
        
    for i in range(N):
        if i not in v and e - K + A[i] >= 500:
            temp = v + [i]
            dfs(cnt+1,temp,e - K + A[i])
            
dfs(0,[],500)
print(result)
