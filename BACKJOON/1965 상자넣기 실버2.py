import sys
N = int(input())
L = list(map(int,input().split()))
dp = [0 for _ in range(0,N)]


R = 0
for i in range(0,N):
    dp[i]= 1
    for j in range(0,i):
        if L[i] > L[j] and dp[j]+1 > dp[i]:
            dp[i] = dp[j] + 1
    R = max(dp[i],R)
print(R)
