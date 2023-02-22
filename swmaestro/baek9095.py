def solution(n):
    if n == 0:
        return 0
    dp = (1,2,4)
    if n < 4:
        return dp[n-1]
    for i in range(4,n+1):
        dp = (dp[1], dp[2], sum(dp))
    return dp[2]
if __name__ == '__main__':
    T = int(input())
    answers = []
    for _ in range(T):
        answers.append(solution(int(input())))
    for answer in answers:
        print(answer)