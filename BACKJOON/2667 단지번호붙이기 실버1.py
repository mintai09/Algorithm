import sys

N = int(input())
G = []

for i in range(N):
    G.append(list(map(int,input())))


step_x = [-1,1,0,0]
step_y = [0,0,-1,1]

homes = []

def dfs(x,y):
    global cnt
    
    if N > x >= 0 and  N > y >= 0:
        if G[y][x] == 1:
            G[y][x] = 2
            cnt += 1
            for i in range(4):
                dfs(x+step_x[i],y+step_y[i])


for i in range(N):
    for j in range(N):
        cnt = 0
        dfs(i,j)
        if cnt != 0:
            homes.append(cnt)

homes.sort()

print(len(homes))

for i in range(len(homes)):
    print(homes[i])
