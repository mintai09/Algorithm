from collections import deque

N,K = map(int,input().split())

heap = []

queue = deque([ i for i in range(1,N+1)])
    
cnt = 1
res = []
while queue:
    pop = queue.popleft()
    if cnt != K:
        queue.append(pop)
    else:
        res.append(pop)
        cnt = 0
    cnt += 1


if len(res) == 1:
    print('<%d>'%res[0])
else:
    print('<%d'%res[0],end=',')

    for i in range(1,N):
        if i == len(res) - 1:
            print('','%d>'%res[i])
        else:
            print('',res[i],end=',')
