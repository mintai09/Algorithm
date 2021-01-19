import sys
import heapq


M,N = map(int,sys.stdin.readline().split())
G = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]


INF = sys.maxsize

move_x = [-1,1,0,0]
move_y = [0,0,-1,1]


     
def dijkstra():

    dist = [[INF]*N for _ in range(M)]
    
    heap = []   
    Node = (0,0)
    
    if G[0][0] == -1 or G[M-1][N-1] == -1:
        return -1
    
    heapq.heappush(heap,(G[0][0],Node))
    
    while heap:
        d,Node = heapq.heappop(heap)

             
        for k in range(4):
            i,j = move_x[k] + Node[0],move_y[k] + Node[1]
            if 0 <= i < M and 0 <= j < N and G[i][j] != -1:

                via = d + G[i][j] 
                if via < dist[i][j]:
                    dist[i][j] = via
                    heapq.heappush(heap,(via,(i,j)))
                
    if dist[M-1][N-1] == INF:
        return -1
    else:
        return dist[M-1][N-1]


print(dijkstra())
