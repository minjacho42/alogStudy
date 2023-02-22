def solution(triangle):
    dp = []
    for i, line in enumerate(triangle):
        newDp = []
        if i == 0:
            dp = line
            continue
        for j, n in enumerate(line):
            if j == 0:
                newDp.append(dp[0]+n)
            elif j == i:
                newDp.append(dp[j-1]+n)
            else:
                newDp.append(max(dp[j-1],dp[j])+n)
        dp = newDp
    return max(dp)

if __name__ == '__main__':
    height = int(input())
    triangle = []
    for _ in range(height):
        triangle.append(list(map(int, input().split())))
    print(solution(triangle))