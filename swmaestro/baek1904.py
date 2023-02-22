#15746으로 나눈 나머지!!!!!
import sys

input = sys.stdin.readline

N = int(input())

if N < 4:
    dp = [0,1,2,3]
    print(dp[N])
else:
    dp = (2,3)
    for i in range(3, N):
        dp = (dp[1], sum(dp))
    print(dp[1]%15746)
