from collections import deque
M,N = map(int,input().split())


step_x = [-1,1,0,0]
step_y = [0,0,-1,1]

def bfs(tomato):
    
    q = deque(tomato)
    
    cnt = len(tomato)
    
    while q:
        x,y,day = q.popleft()
        
        
        for i in range(4):
            if M > x + step_x[i] >=0 and N > y + step_y[i] >=0 and G[y + step_y[i]][x + step_x[i]] == 0:
                cnt += 1
                G[y + step_y[i]][x + step_x[i]] = 1
                q.append((x + step_x[i],y + step_y[i],day+1))
                if cnt == max_tomato :
                    return day + 1
        
    else:
        if cnt == max_tomato :
            return 0
        else:
            return -1
    
    return day
    
G = [[] for i in range(N)]

for i in range(N):
    G[i] = list(map(int,input().split()))

tomato = []
max_tomato = M*N

for i in range(N):
    for j in range(M):
        if G[i][j] == 1:
            tomato.append((j,i,0))
        elif G[i][j] == -1:
            max_tomato -= 1
            
print(bfs(tomato))
