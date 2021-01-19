from collections import deque

M,N,H = map(int,input().split())


step_x = [-1,1,0,0,0,0]
step_y = [0,0,-1,1,0,0]
step_z = [0,0,0,0,-1,1]


def bfs(tomato):
    
    q = deque(tomato)
    
    cnt = len(tomato)
    
    while q:
        x,y,z,day = q.popleft()
        
        if cnt == max_tomato :
            return day
        
        for i in range(6):
            if H > z + step_z[i] >= 0 and M > x + step_x[i] >=0 and N > y + step_y[i] >=0 and G[z + step_z[i]][y + step_y[i]][x + step_x[i]] == 0:
                cnt += 1
                G[z + step_z[i]][y + step_y[i]][x + step_x[i]] = 1
                q.append((x + step_x[i],y + step_y[i],z + step_z[i],day+1))
                if cnt == max_tomato :
                    return day + 1
                
        
    else:
        if cnt == max_tomato :
            return 0
        else:
            return -1
    
    return day
    
G = [[[]for i in range(N)] for i in range(H)]

for i in range(H):
    for j in range(N):
        G[i][j] = list(map(int,input().split()))

tomato = []
max_tomato = M*N*H

for i in range(H):
    for j in range(N):
        for k in range(M):
            if G[i][j][k] == 1:
                tomato.append((k,j,i,0))
            elif G[i][j][k] == -1:
                max_tomato -= 1
            
print(bfs(tomato))
