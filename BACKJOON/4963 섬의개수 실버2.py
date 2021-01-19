import sys

step_x = [-1, 1, 0, 0, -1, 1, -1, 1]
step_y = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(x,y):
    
    visit[y][x] = 1
    
    for i in range(8):
        move_x = x + step_x[i]
        move_y = y + step_y[i]
        
        if 0 <= move_y < h and 0 <= move_x < w and visit[move_y][move_x] == False and island[move_y][move_x] == 1:
            island[move_y][move_x] = 0
            dfs(move_x,move_y)

while 1:
    
    w,h = map(int,input().split())
    
    if w == 0 and h == 0:
        break
    
    visit = [[False] * w for _ in range(h)]
    island = [ list(map(int,input().split())) for _ in range(0,h)]

    R = 0
    
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1 and visit[i][j] == False:
                dfs(j,i)
                R += 1
    print(R)
