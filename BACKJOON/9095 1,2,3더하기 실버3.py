n = int(input())

nums = []

for i in range(n):
    num = int(input())
    nums.append(num)
    

m = max(nums) 
dp = [0 for _ in range(m)]

for i in range(m):
    if i >= 3:
        dp[i] = sum(dp[i-3:i])
    else:
         dp[i] = sum(dp[:i]) + 1
         
for i in nums:
    print(dp[i-1])
