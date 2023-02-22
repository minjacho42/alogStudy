def solution(n):
    dp = (1, 2)
    if n < 3:
        return dp[n-1]
    for _ in range(3, n+1):
        dp = (dp[1], sum(dp))
    return dp[1]%10007
if __name__ == '__main__':
    n = int(input())
    print(solution(n))