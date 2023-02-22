
def re_solution(n, stairs, before):
    # before 이 true이면 한칸 내려가기 두칸 내려가기 모두 가능.
    if n == 1:
        return stairs[0]
    elif n == 0:
        return 0
    if before:
        return max(re_solution(n-1, stairs, False), re_solution(n-2, stairs, True)) + stairs[n-1]
    else:
        return re_solution(n-2, stairs, True) + stairs[n-1]

def dp_solution(n, stairs):
    dp = []
    if n > 0:
        dp.append(stairs[0])
    if n > 1:
        dp.append(stairs[0]+stairs[1])
    if n > 2:
        dp.append(max(stairs[0],stairs[1])+stairs[2])
    if n > 3:
        for i in range(3,n):
            dp.append(max(dp[i-3]+stairs[i-1], dp[i-2])+stairs[i])
    return dp[len(dp) - 1]

if __name__ == '__main__':
    n = int(input())
    stairs = []
    for _ in range(n):
        stairs.append(int(input()))
    #print(re_solution(n, stairs, True))
    print(dp_solution(n, stairs))
