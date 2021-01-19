T = int(input())

step_x = [-1,1,0,0]
step_y = [0,0,-1,1]

def dfs(x,y):
    
    stack = []
    stack.append((x,y))

    while stack:
        x,y = stack.pop()
        for i in range(4):
            if M > x + step_x[i] >=0 and N > y + step_y[i] >=0 and G[y + step_y[i]][x + step_x[i]]:
                G[y + step_y[i]][x + step_x[i]] = 0
                stack.append((x + step_x[i],y + step_y[i]))
            
for i in range(T):
    M,N,K = map(int,input().split())
    G = [[0 for _ in range(M)]for _ in range(N)]
    
    for i in range(K):
        x,y = map(int,input().split())
        G[y][x] = 1
    cnt = 0
    
    for i in range(N):
        for j in range(M):
            if G[i][j] == 1:
                G[i][j] = 0
                dfs(j,i)
                cnt += 1       
    print(cnt)
                
