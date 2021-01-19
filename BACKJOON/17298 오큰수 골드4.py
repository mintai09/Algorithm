import sys
from collections import deque

n=int(sys.stdin.readline())
seq_li=list(map(int,sys.stdin.readline().split()))
q=deque()
ans=deque()

for j in range(n):
    i = n - j -1
    while q:
        if q[-1]<=seq_li[i]:
            q.pop()
        else:
            ans.appendleft(str(q[-1]))
            q.append(seq_li[i])
            break

    if len(q)==0:
        ans.appendleft(str(-1))
        q.append(seq_li[i])

print(' '.join(ans))
