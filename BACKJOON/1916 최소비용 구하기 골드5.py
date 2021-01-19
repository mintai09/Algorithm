import sys
import heapq

N = int(input())
M = int(input())

G = [[]for i in range(N+1)]

for i in range(M):
    u,v,w = map(int,input().split())
    G[u].append((v,w))
    
s,e = map(int,input().split())

INF = sys.maxsize

def dijkstra():
    dist = [ INF for i in range(0,N+1)]
    
    heap = []
    dist[s] = 0
    
    heapq.heappush(heap,(0,s))
    
    while heap:
        cur_w,cur_v = heapq.heappop(heap)

        if dist[cur_v] < cur_w:
            continue
        
        for n in G[cur_v]:
            new_w = cur_w + n[1]
            if dist[n[0]] > new_w:
                dist[n[0]] = new_w
                heapq.heappush(heap,(new_w,n[0]))

    return dist[e]

print(dijkstra())
