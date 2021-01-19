from collections import deque

N,K = map(int,input().split())

visited = [0 for _ in range(200001)]

def bfs(): 
    q = deque([N])
    
    while q:
        x = q.popleft()
        time = visited[x] + 1
        case = [x+1,x-1,2*x]
        
        for xx in case:
            
            if x  == K:
                print(time-1)
                break

            if xx >= 0 and xx <= 200000 and visited[xx] == 0 and xx != N:
                visited[xx] = time
                q.append(xx)
bfs()


