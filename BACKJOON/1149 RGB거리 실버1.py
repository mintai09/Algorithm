import sys
N = int(input())
INF = sys.maxsize

dp = [[INF,INF,INF]for i in range(0,N+1)]

house = []
r,g,b = map(int,input().split())

dp[0][0] = r
dp[0][1] = g
dp[0][2] = b

for i in range(0,N-1):
    r,g,b = map(int,input().split())
    
    dp[i+1][0] = min(dp[i][1],dp[i][2]) + r
    dp[i+1][1] = min(dp[i][0],dp[i][2]) + g
    dp[i+1][2] = min(dp[i][0],dp[i][1]) + b
    
print(min(dp[N-1]))
