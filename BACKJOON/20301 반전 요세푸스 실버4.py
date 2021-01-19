from collections import deque

N,K,M = map(int,input().split())

heap = []

queue = deque([ i for i in range(1,N+1)])
    
cnt = 1
res = []
turn = 1

cnt2 = 0
while queue:


    if turn == 1:
        pop = queue.popleft()
    else:
        pop = queue.pop()
        
        
    if cnt != K:
        if turn == 1:
            queue.append(pop)
        else:
            queue.appendleft(pop)
    else:
        res.append(pop)
        cnt = 0
        cnt2 += 1
        
    if cnt2 == M:
        turn *= -1
        cnt2 = 0
        
    cnt += 1

for i in res:
    print(i)
