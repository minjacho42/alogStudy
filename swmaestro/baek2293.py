import sys

input = sys.stdin.readline

n, k = tuple(map(int, input().split()))
coins = []
for _ in range(n):
    coin = int(input())
    if coin > k:
        continue
    else:
        coins.append(coin)
def solution(coins, k):
    table = [0 for _ in range(k+1)]
    for coin in sorted(coins):
        for value in range(coin, k+1):
            if value == coin:
                table[value] += 1
                continue
            table[value] += table[value-coin]
    return table[k]

print(solution(coins,k))
