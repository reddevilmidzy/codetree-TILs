INF = int(1e9)
n = int(input())
dp = [INF]*(max(5, n)+1)
dp[3] = 1
dp[5] = 1

for i in range(6, n+1):
    dp[i] = min(dp[i-3] + 1, dp[i-5] + 1, dp[i])

print(dp[n] if dp[n] != INF else -1)