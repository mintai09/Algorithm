N,M = map(int,input().split())

def dfs(V):
    if len(V) == M:
        
        print(' '.join(V))
    else:
        for i in range(1,N+1):
            dfs(V+[str(i)])          
dfs([])
