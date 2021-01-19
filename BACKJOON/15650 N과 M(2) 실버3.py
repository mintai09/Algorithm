N,M = map(int,input().split())

def dfs(V,s):
    if len(V) == M:
        
        print(' '.join(V))
    else:
        for i in range(s,N+1):
            if str(i) not in V:
                dfs(V+[str(i)],i)          
dfs([],1)
