N = int(input())

dp = [0, [1]]

for i in range(2, N+1):
    can = []
    if i % 2 == 0:
        can.append(i//2)
    if i % 3 == 0:
        can.append(i//3)
    can.append(i-1)
    dp.append(dp[min(can, key=lambda x: len(dp[x]))] + [i])

print(len(dp[N])-1)
print(' '.join(list(map(str, dp[N][::-1]))).strip())