def solution(costs):
    length = len(costs)
    dp = costs[0]
    for i in range(1, length):
        dp = (costs[i][0] + min(dp[1],dp[2]), costs[i][1] + min(dp[0],dp[2]), costs[i][2] + min(dp[0],dp[1]))
    return min(dp)

if __name__ == '__main__':
    N = int(input())
    costs = []
    for _ in range(N):
        costs.append(list(map(int, input().split())))
    print(solution(costs))