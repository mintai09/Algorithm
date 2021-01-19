a = int(input())
Dp = [  -1 for _ in range(0,1000001)]
Dp[0] = 0
Dp[1] = 1
Dp[2] = 2
i = 3

while i <= a:
    Dp[i] = (Dp[i-1] + Dp[i-2]) % 15746
    i += 1
print(Dp[a])
