import sys
import heapq

V,E = map(int,input().split())

K = int(input())

G = [[] for _ in range(0,V+1)]

for i in range(E):
    edge = list(map(int,input().split()))
    G[edge[0]].append([edge[1],edge[2]])
    
INF = sys.maxsize


def daijkstra():

    dist = [ INF for _ in range(0,V+1)]
    dist[K] = 0
    heap = []
    heapq.heappush(heap,[dist[K],K])
    
    while heap:
        cur_w , cur_v = heapq.heappop(heap)
        
        if dist[cur_v] < cur_w:
            continue
        
        for n in G[cur_v]:
            new_w = cur_w + n[1]
            if dist[n[0]] > new_w:
                dist[n[0]] = new_w
                heapq.heappush(heap,[new_w,n[0]])
                
    return dist
dist = daijkstra()

for i in range(1,V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
