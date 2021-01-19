import sys
import heapq

N,M,X = map(int,input().split())

G = [[]for _ in range(0,N+1)]

for _ in range(M):
    u,v,w = map(int,input().split())
    G[u].append((v,w))

INF = sys.maxsize
def dijkstra(start):
    heap = []
    dist = [INF for i in range(0,N+1)]
    dist[start] = 0
    
    heapq.heappush(heap,(0,start))
    
    while heap:
        cur_w , cur_v = heapq.heappop(heap)
        
        if dist[cur_v] < cur_w:
            continue
        
        for v in G[cur_v]:
            new_w = cur_w + v[1]
            if new_w < dist[v[0]]:
                dist[v[0]] = new_w
                heapq.heappush(heap,(new_w,v[0]))
    return dist

def result():
    dist = []
    dist.append([])
    
    come = dijkstra(X)
    cost = []
    
    for i in range(1,N+1):
        if i != X:
            go = dijkstra(i)
            cost.append(go[X] + come[i])
            
    return max(cost)    
print(result())
