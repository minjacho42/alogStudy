from math import gcd

n = int(input())
trees = [int(input()) for __ in range(n)]
g = gcd(*list(map(lambda x: trees[x] - trees[x-1], range(1,n))))
print(len(range(trees[0], trees[n-1] + 1, g)) - len(trees))