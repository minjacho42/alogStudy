import sys

input = sys.stdin.readline

N = int(input())

def solution(n):
    dp = (1, 1, 1)
    for _ in range(n-1):
        dp = (sum(dp)%9901, (dp[0]+dp[1])%9901, (dp[0]+dp[2])%9901)
    return sum(dp)%9901

print(solution(N))