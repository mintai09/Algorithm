a = int(input())
Dp = [  -1 for _ in range(0,a+1)]
Dp[0] = 0
Dp[1] = 1
i = 2

while i <= a:
    Dp[i] = Dp[i-1] + Dp[i-2]
    i += 1
print(Dp[a])
