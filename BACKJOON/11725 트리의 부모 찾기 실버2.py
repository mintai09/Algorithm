import sys



def dfs():
    stack = [1]
    while(stack):
        v = stack.pop()
        for i in G[v]:
            P[i] = v
            stack.append(i)
            G[i].remove(v)
            
N = int(input())

G = [[]for _ in range(N+1)]
P = [ 0 for _ in range(N+1)]

for i in range(N-1):
    V1,V2 = map(int,input().split())
    G[V1].append(V2)
    G[V2].append(V1)

dfs()

for i in range(2,N+1):
    print(P[i])
