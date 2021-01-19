from collections import deque
N,M = map(int,input().split())


step_x = [-1,1,0,0]
step_y = [0,0,-1,1]

def bfs(x,y):
    
    q = deque([])
    q.append((x,y,0))
    res = 10000
    
    while q:
        x,y,cnt = q.popleft()
        
        if x == M - 1 and y == N - 1:
            res = min(res,cnt)
            
        for i in range(4):
            if M > x + step_x[i] >=0 and N > y + step_y[i] >=0 and G[y + step_y[i]][x + step_x[i]]:
                G[y + step_y[i]][x + step_x[i]] = 0
                q.append((x + step_x[i],y + step_y[i],cnt+1))
                
    return res
    
G = [[] for i in range(N)]

for i in range(N):
    G[i] = list(map(int,input()))
    

print(bfs(0,0)+1)
