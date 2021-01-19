N,K = map(int,input().split())

A = []
for i in range(N):
    A.append(int(input()))


res = 0
for i in range(1,N+1):
    if K == 0:
        break
    if K > A[N-i]:
        cnt = K // A[N-i]
        K -=  cnt * A[N-i]
        res += cnt
        
print(res)
